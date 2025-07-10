from enum import Enum
import logging
from registry.register import register
from repo.sql.sqlite_engine import session
from repo.sql.models.dac import Dac
from repo.sql.models.dsp import Dsp
from repo.sql.models.system import System
from repo.init_data import init_data


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
                dt = tbl()
                setattr(dt, addr, val)
                s.add(dt)
            s.commit()

    def read(self, addr):
        return self.get_table_or_value(addr, SQL_ACCESS_TYPE.READ)

    def get_table_or_value(self, column, type: SQL_ACCESS_TYPE):
        # start reading from largest to smallest table. Performance is negligible for one user.
        with session() as s:
            value = None
            table_found = False
            try:
                value = s.query(getattr(Dac, column)).scalar()
                tbl = Dac
                table_found = True
            except AttributeError as e:
                pass
            if not table_found:
                try:
                    value = s.query(getattr(System, column)).scalar()
                    tbl = System
                    table_found = True
                except AttributeError as e:
                    pass
            if not table_found:
                try:
                    value = s.query(getattr(Dsp, column)).scalar()
                    tbl = Dsp
                    table_found = True
                except AttributeError as e:
                    pass
        if type == SQL_ACCESS_TYPE.GET_TABLE:
            return tbl
        else:
            return value

    def initialize(self):
        for key, value in init_data.items():
            if self.read(key) is None:
                self.write(key, value)
                print("inserting record")
