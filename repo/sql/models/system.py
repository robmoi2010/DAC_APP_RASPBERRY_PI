from sqlalchemy import Column, Integer
from repo.sql.models.base import Base
from repo.sql.sqlite_engine import engine


class System(Base):
    __tablename__ = "system"
    id = Column(Integer, primary_key=True, nullable=False)
    CURRENT_MUSES_VOLUME = Column(Integer)
    CURRENT_VOLUME_DEVICE = Column(Integer)
    VOLUME_ALGORITHM = Column(Integer)
    CURRENT_ALPS_VOLUME = Column(Integer)
    VOLUME_RAMP_ENABLED = Column(Integer)


Base.metadata.create_all(bind=engine)
