import asyncio
import inspect
from queue import Empty, Queue
from threading import Thread
import time
import traceback
from typing import Any


# Configuration
QUEUE_TIMEOUT_SECONDS = 10

# Global state
registry: dict[str, type] = {}
instances: dict[str, Any] = {}
object_factory_queue = Queue()

# ------------------------------
# Registration & Dependency Logic
# ------------------------------


def register(cls: type):
    """Registers a class for dependency injection."""
    registry[cls.__name__.lower()] = cls
    return cls


def get_dependencies(name: str) -> list[str]:
    """Extracts constructor dependencies from type hints."""
    cls = registry.get(name)
    if not cls:
        raise ValueError(f"No class registered under name '{name}'")

    constructor = inspect.signature(cls.__init__)
    deps = []
    for param in constructor.parameters.values():
        if param.name == "self":
            continue
        if param.annotation == inspect.Parameter.empty:
            continue
        dep_name = param.annotation.__name__.lower()
        deps.append(dep_name)
    return deps


# ------------------------------
# Async Public Interface
# ------------------------------


async def get_instance(name: str, force_new=False) -> Any:

    name = name.lower()
    if name in instances and not force_new:
        return instances[name]

    if name not in instances or force_new:
        object_factory_queue.put(name)

    try:
        async with asyncio.timeout(QUEUE_TIMEOUT_SECONDS):
            while name not in instances:
                await asyncio.sleep(0.1)
            return instances[name]
    except asyncio.TimeoutError:
        print(f"[get_instance] Timeout while waiting for instance of '{name}'")
        return None


# ------------------------------
# Internal Instance Creation
# ------------------------------


def _new_instance(name: str, force_new=False) -> Any:
    name = name.lower()
    print(f"[new_instance] Creating instance for '{name}'")
    if name in instances and not force_new:
        print(f"[new_instance] Returning cached instance for '{name}'")
        return instances[name]

    cls = registry.get(name)
    if not cls:
        raise ValueError(f"No class registered under name '{name}'")

    try:
        dep_names = get_dependencies(name)
        deps = [_new_instance(dep) for dep in dep_names]
        instance = cls(*deps)
        instances[name] = instance
        print(f"[new_instance] Successfully created '{name}' id: {id(instances[name])}")
        return instance
    except Exception as e:
        print(f"[new_instance ERROR] Failed to create '{name}': {e}")
        traceback.print_exc()
        raise


# ------------------------------
# Queue Consumer (Runs in Thread)
# ------------------------------


def object_queue_consumer():
    print("[consumer] Thread started")
    while True:
        try:
            name = object_factory_queue.get(block=True)
            print(f"[consumer] Received creation request for '{name}'")
            instance = _new_instance(name, force_new=True)
            print(f"[consumer] Created instance for '{name}'")
        except Exception as e:
            print(f"[consumer ERROR] While creating '{name}': {e}")
        finally:
            time.sleep(0.1)


# ------------------------------
# Initialization
# ------------------------------


def start_consumer():
    thread = Thread(target=object_queue_consumer, daemon=True)
    thread.start()
