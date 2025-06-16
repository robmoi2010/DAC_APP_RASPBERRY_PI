import inspect


registry = {}
instances = {}


def register(cls):
    id = cls.__name__.lower()
    registry[id] = cls
    return cls


def get_dependencies(nm):
    dependecies = []
    constructor = inspect.signature(registry[nm].__init__)
    for name, param in constructor.parameters.items():
        if name == "self":
            continue
        if param.annotation == inspect.Parameter.empty:
            continue
        param_name = param.annotation.__name__.lower()
        dependecies.append(param_name)
    return dependecies


def get_instance(name, composed_obj: list[str] = None, force_new=False):
    if name not in registry:
        raise ValueError(f"No class registered under name '{name}'")
    if name not in instances or force_new:
        if composed_obj is None:
            # get object dependencies for automatic dependency injection
            dependencies = get_dependencies(name)
            if dependencies is not None and len(dependencies) > 0:
                composed_obj = dependencies
        if composed_obj is not None:
            # create objects from the list of names
            obj = []
            for ob in composed_obj:
                obj.append(get_instance(ob))
            instances[name] = registry[name](*obj)
        else:
            instances[name] = registry[name]()
    return instances[name]
