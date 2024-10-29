from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP
from . import Base

class SensorData(Base):
    __tablename__ = 'event_up'
    deduplication_id = Column(Integer, primary_key=True, index=True)
    dev_eui = Column(String(80), index=True)
    application_id = Column(String(80), index=True)
    device_profile_id = Column(String(80), index=True)
    time = Column(TIMESTAMP(timezone=True), index=True)
    object = Column(JSON)
    device_name = Column(String(80), index=True)
