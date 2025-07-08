from enum import Enum
import logging
from registry.register import register
from repo.sql.sqlite_engine import session
from repo.sql.models.dac import Dac
from repo.sql.models.dsp import Dsp
from repo.sql.models.system import System


class SQL_ACCESS_TYPE(Enum):
    READ = 0
    GET_TABLE = 1


@register
class SqlStorage:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def write(self, addr, val):
        tbl = self.get_table_or_value(addr, SQL_ACCESS_TYPE.GET_TABLE)
        with session() as s:
            row = s.query(tbl).first()
            if row:
                setattr(row, addr, val)
            else:
                dt=tbl()
                setattr(dt, addr, val)
                s.add(dt)
            s.commit()

    def read(self, addr):
        return self.get_table_or_value(addr, SQL_ACCESS_TYPE.READ)

    def get_table_or_value(self, column, type: SQL_ACCESS_TYPE):
        # start reading from largest to smallest table. Performance is negligible for one user.
        with session() as s:
            value = None
            table_found=False
            try:
                value = s.query(getattr(Dac, column)).scalar()
                tbl = Dac
                table_found=True
            except AttributeError as e:
                pass
            if not table_found:
                try:
                    value = s.query(getattr(System, column)).scalar()
                    tbl = System
                    table_found=True
                except AttributeError as e:
                    pass
            if not table_found:
                try:
                    value = s.query(getattr(Dsp, column)).scalar()
                    tbl = Dsp
                    table_found=True
                except AttributeError as e:
                    pass
        if type == SQL_ACCESS_TYPE.GET_TABLE:
            return tbl
        else:
            return value

    def initialize(self):
        data = {
            "KNOB_BUTTON_MODE": 0,
            "DISABLE_VOLUME": 0,
            "CURRENT_FILTER": 2,
            "CURRENT_DAC_MODE": 2,
            "DAC_MUTED": 0,
            "CURRENT_VOLUME": 128.5,
            "CURRENT_MUSES_VOLUME": -25,
            "CURRENT_INPUT": 4,
            "CURRENT_MAIN_OUTPUT": 3,
            "CURRENT_SUBWOOFER_OUTPUT": 2,
            "MAINS_INPUT_SINK": 2,
            "SUBWOOFER_INPUT_SINK": 2,
            "SUBWOOFER_OUTPUT_SOURCE": 2,
            "MAINS_OUTPUT_SOURCE": 1,
            "SOUND_MODE": 2,
            "SECOND_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COMPENSATION_ENABLED": 1,
            "THIRD_ORDER_COEFFICIENTS_STORED": 0,
            "SECOND_ORDER_COEFFICIENTS_STORED": 0,
            "CURRENT_VOLUME_DEVICE": 0,
            "VOLUME_ALGORITHM": 0,
            "SECOND_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "SECOND_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_1": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_2": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_3": "0110",
            "THIRD_ORDER_ENABLE_COEFFICIENTS_4": "0110",
            "CURRENT_ALPS_VOLUME": 0,
            "OVERSAMPLING_ENABLED": 1,
        }
        for key, value in data.items():
            if self.read(key) is None:
                self.write(key, value)
                print("inserting record")
