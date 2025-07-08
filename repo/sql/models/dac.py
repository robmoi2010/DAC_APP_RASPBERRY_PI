from sqlalchemy import Column, Integer
from repo.sql.models.base import Base
from repo.sql.sqlite_engine import engine


class Dac(Base):
    __tablename__ = "dac"
    id = Column(Integer, primary_key=True, nullable=False)
    KNOB_BUTTON_MODE = Column(Integer)
    DISABLE_VOLUME = Column(Integer)
    CURRENT_FILTER = Column(Integer)
    CURRENT_DAC_MODE = Column(Integer)
    DAC_MUTED = Column(Integer)
    CURRENT_VOLUME = Column(Integer)
    SECOND_ORDER_COMPENSATION_ENABLED = Column(Integer)
    THIRD_ORDER_COMPENSATION_ENABLED = Column(Integer)
    THIRD_ORDER_COEFFICIENTS_STORED = Column(Integer)
    SECOND_ORDER_COEFFICIENTS_STORED = Column(Integer)
    SECOND_ORDER_ENABLE_COEFFICIENTS_1 = Column(Integer)
    SECOND_ORDER_ENABLE_COEFFICIENTS_2 = Column(Integer)
    SECOND_ORDER_ENABLE_COEFFICIENTS_3 = Column(Integer)
    SECOND_ORDER_ENABLE_COEFFICIENTS_4 = Column(Integer)
    THIRD_ORDER_ENABLE_COEFFICIENTS_1 = Column(Integer)
    THIRD_ORDER_ENABLE_COEFFICIENTS_2 = Column(Integer)
    THIRD_ORDER_ENABLE_COEFFICIENTS_3 = Column(Integer)
    THIRD_ORDER_ENABLE_COEFFICIENTS_4 = Column(Integer)
    OVERSAMPLING_ENABLED = Column(Integer)


Base.metadata.create_all(bind=engine)
