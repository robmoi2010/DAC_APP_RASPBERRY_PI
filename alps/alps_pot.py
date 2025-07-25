from time import sleep
from gpiozero import Motor
import configs.app_config as app_config
from dac.dac_volume import DacVolume
from registry.register import register
from repo.storage import Storage
from services.utils.ws_connection_manager import WSConnectionManager
from volume.abstract_volume import AbstractVolume
from volume.volume_util import (
    CURRENT_ALPS_VOLUME_ID,
    VOL_DIRECTION,
    VOLUME_ALGORITHM,
    VOLUME_DEVICE,
    remap_value,
)


@register
class AlpsPot(AbstractVolume):
    def __init__(self, storage: Storage, connection_manager: WSConnectionManager):
        self.config = app_config.getConfig()["ALPS"]
        self.storage = storage
        # self.motor = Motor(
        #     forward=self.config["FORWARD_GPIO_PIN"],
        #     backward=self.config["BACKWARD_GPIO_PIN"],
        # )
        self.connection_manager = connection_manager

    def update_volume(
        self, direction: VOL_DIRECTION, volume_algorithm: VOLUME_ALGORITHM
    ):
        step = self.config["STEP"]
        current = self.get_current_volume()
        if direction == VOL_DIRECTION.UP:
            current += step
        elif direction == VOL_DIRECTION.DOWN:
            current -= step
        if current > 100:
            current = 100
        if current < 0:
            current = 0
        # self.update_motor_volume_position(direction, current)
        return self.process_new_volume(current, volume_algorithm)

    def update_motor_volume_position(self, direction: VOL_DIRECTION, volume):
        # remap volume from 0-100 to adc min-max
        adc_value = remap_value(
            volume, 0, 100, self.config["ADC_MIN_VALUE"], self.config["ADC_MAX_VALUE"]
        )
        current_pot_value = self.get_current_adc_pot_value()
        while (direction == VOL_DIRECTION.UP and adc_value < current_pot_value) or (
            direction == VOL_DIRECTION.DOWN and adc_value > current_pot_value
        ):
            if direction == VOL_DIRECTION.UP:
                self.move_motor_foward()
            else:
                self.move_motor_back()
            current_pot_value = self.get_current_adc_pot_value()

    def mute(self):
        # mute at the dac level
        volume: DacVolume = register.get_instance("dacvolume")
        volume.mute()

    def get_percentage_volume(self, vol):
        return vol

    def get_current_volume(self):
        return self.storage.read(CURRENT_ALPS_VOLUME_ID)

    def persist_volume(self, volume):
        self.storage.write(CURRENT_ALPS_VOLUME_ID, volume)

    def move_motor_foward(self):
        self.motor.forward()
        sleep(self.config["MOTOR_STEP_MILLIS"] / 1000)
        self.motor.stop()

    def move_motor_back(self):
        self.motor.backward()
        sleep(self.config["MOTOR_STEP_MILLIS"] / 1000)
        self.motor.stop()

    def poll_adc_pot_value(self):
        # poll for manual rotation of volume knob and update volume displayed in the ui.
        current = self.get_current_adc_pot_value()
        current_volume = self.get_current_volume()
        new_volume = remap_value(
            current, self.config["ADC_MIN_VALUE"], self.config["ADC_MAX_VALUE"], 0, 100
        )
        if current_volume != new_volume:
            self.process_new_volume(new_volume, None)
        sleep(self.config["POLL_MILLIS"] / 1000)

    def get_current_adc_pot_value(self):
        # get current positional value from adc via spi or i2c
        return 50

    def update_ui_volume(self, volume):
        return super().update_ui_volume(
            VOLUME_DEVICE.ALPS, self.connection_manager, volume
        )

    def disable_enable_volume(self, selected, volume_algorithm: VOLUME_ALGORITHM):
        pass

    def is_volume_disabled(self):
        pass

    def process_new_volume(self, currVol, volume_algorithm: VOLUME_ALGORITHM):
        self.persist_volume(currVol)
        self.update_ui_volume(currVol)

    def get_volume_from_percentage(self, percentage):
        pass

    def get_max_volume(self, percentage):
        return 100

    def get_min_volume(self, percentage):
        return 0

    def is_volume_more_than(self, volume1, volume2):
        return volume1 > volume2
