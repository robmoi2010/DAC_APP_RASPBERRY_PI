from sqlalchemy import Column, Integer
from repo.sql.models.base import Base
from repo.sql.sqlite_engine import engine


class Dsp(Base):
    __tablename__ = "dsp"
    id = Column(Integer, primary_key=True, nullable=False)
    CURRENT_INPUT = Column(Integer)
    CURRENT_MAIN_OUTPUT = Column(Integer)
    CURRENT_SUBWOOFER_OUTPUT = Column(Integer)
    MAINS_INPUT_SINK = Column(Integer)
    SUBWOOFER_INPUT_SINK = Column(Integer)
    SUBWOOFER_OUTPUT_SOURCE = Column(Integer)
    MAINS_OUTPUT_SOURCE = Column(Integer)
    SOUND_MODE = Column(Integer)


Base.metadata.create_all(bind=engine)
