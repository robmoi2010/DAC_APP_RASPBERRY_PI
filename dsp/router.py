from enum import Enum
import repo.storage as storage

MAINS_OUTPUT_SOURCE_ID = "MAINS_OUTPUT_SOURCE"
SUBWOOFER_OUTPUT_SOURCE_ID = "SUBWOOFER_OUTPUT_SOURCE"
MAINS_INPUT_SINK_ID = "MAINS_INPUT_SINK"
SUBWOOFER_INPUT_SINK_ID = "SUBWOOFER_INPUT_SINK"


class RouteSources(Enum):
    INPUT = (0,)
    DSP_CORE = (1,)
    ASRC = 2


class RouteSinks(Enum):
    OUTPUT = (0,)
    DSP_CORE = (1,)
    ASRC = 2 


def update_mains_output_source(source):
    storage.write(MAINS_OUTPUT_SOURCE_ID, source)


def update_subwoofer_output_source(source):
    storage.write(SUBWOOFER_OUTPUT_SOURCE_ID, source)


def update_mains_input_sink(sink):
    storage.write(MAINS_INPUT_SINK_ID, sink)


def update_subwoofer_input_sink(sink):
    storage.write(SUBWOOFER_INPUT_SINK_ID, sink)


def get_mains_output_source():
    return storage.read(MAINS_OUTPUT_SOURCE_ID)


def get_subwoofer_output_source():
    return storage.read(SUBWOOFER_OUTPUT_SOURCE_ID)


def get_mains_input_sink():
    return storage.read(MAINS_INPUT_SINK_ID)


def get_subwoofer_input_sink():
    return storage.read(SUBWOOFER_INPUT_SINK_ID)
