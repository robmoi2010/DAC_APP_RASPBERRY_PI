from registry.register import get_instance
from model.model import ResponseModel
from services.utils.system_util import is_selected

dac_filters = get_instance("dacfilters")
dac = get_instance("dac")
volume_encoder = get_instance("volumeencoder")


def create_filter_response():
    # 0 Minimum phase
    # 1 Linear phase apodizing fast roll-off
    # 2 Linear phase fast roll-off
    # 3 Linear phase fast roll-off low-ripple
    # 4 Linear phase slow roll-off
    # 5 Minimum phase fast roll-off
    # 6 Minimum phase slow roll-off
    # 7 Minimum phase slow roll-off low dispersion
    current_filter = dac_filters.get_current_filter()
    list = []
    r0 = ResponseModel(
        key="0",
        value="" + is_selected(current_filter, 0),
        description="Version 2 of minimum phase fast roll-off with less ripple and more image rejection",
        display_name="Minimum phase",
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value="" + is_selected(current_filter, 1),
        description="Full image rejection by fs/2 to avoid any aliasing, with smooth roll-of starting before 20k",
        display_name="Linear phase apodizing first roll-off",
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value="" + is_selected(current_filter, 2),
        description="Sabre legacy filter, optimized for image rejection @0.55 fs",
        display_name="Linear phase fast roll-off",
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3",
        value="" + is_selected(current_filter, 3),
        description="Sabre legacy filter, optimized for in-band ripple",
        display_name="Linear phase fast roll-off low ripple",
    )
    list.append(r3)
    r4 = ResponseModel(
        key="4",
        value="" + is_selected(current_filter, 4),
        description="Sabre legacy filter, optimized for low latency, but symmetric impulse response",
        display_name="Linear phase slow roll-off",
    )
    list.append(r4)
    r5 = ResponseModel(
        key="5",
        value="" + is_selected(current_filter, 5),
        description="Low latency, minimal pre ringing and low passband ripple, image rejection @0.55fs",
        display_name="Minimum phase fast roll-off",
    )
    list.append(r5)
    r6 = ResponseModel(
        key="6",
        value="" + is_selected(current_filter, 6),
        description="Lowest latency at the cost of image rejection",
        display_name="Minimum phase slow roll-off",
    )
    list.append(r6)
    r7 = ResponseModel(
        key="7",
        value="" + is_selected(current_filter, 7),
        description="Provides a nice balance of the low latency of minimum phase filters and the low dispersion of linear phase filters. "
        "Minimal pre-ringing is added to achieve the low dispersion in the audio band.",
        display_name="Minimum phase slow roll-off low dispersion",
    )
    list.append(r7)
    return list


def create_dac_mode_response():
    # 0 I2S Slave mode
    # 1 LJ Slave mode
    # 2 I2S Master mode
    # 3 SPDIF mode
    list = []
    current_dac_mode = dac.get_current_dac_mode()
    r0 = ResponseModel(
        key="0",
        value=is_selected(current_dac_mode, 0),
        description="I2S input, source provides the clock signal",
        display_name="I2S Slave Mode",
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(current_dac_mode, 1),
        description="TDM left justified, source provides the clock signal",
        display_name="LJ Slave mode",
    )
    list.append(r1)
    r2 = ResponseModel(
        key="2",
        value=is_selected(current_dac_mode, 2),
        description="I2S input, the Dac provides the clock signal",
        display_name="I2S Master mode",
    )
    list.append(r2)
    r3 = ResponseModel(
        key="3",
        value=is_selected(current_dac_mode, 3),
        description="Toslink or coaxial input",
        display_name="SPDIF mode",
    )
    list.append(r3)
    return list


def create_volume_modes_response():
    list = []
    selected = volume_encoder.getButtonKnobMode()
    r0 = ResponseModel(
        key="0",
        value=is_selected(selected, 0),
        description="Sets volume knob press button to mute device",
        display_name="Mute",
    )
    list.append(r0)
    r1 = ResponseModel(
        key="1",
        value=is_selected(selected, 1),
        description="Sets volume knob press button to disable dac volume(sets to max)",
        display_name="Disable/enable Volume",
    )
    list.append(r1)
    return list
