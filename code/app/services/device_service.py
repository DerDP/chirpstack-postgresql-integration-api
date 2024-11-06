from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.sensor_data import SensorData
from typing import Optional


# Service for Endpoint to get all devices with pagination


def get_devices(db: Session, dev_eui: Optional[str], application_id: Optional[str], device_profile_id: Optional[str], skip: int = 0, limit: int = 10):
    try:
        filter = [SensorData.object != '{}']
        if dev_eui:
            filter.append(SensorData.dev_eui == dev_eui)
        if application_id:
            filter.append(SensorData.application_id == application_id)
        if device_profile_id:
            filter.append(SensorData.device_profile_id == device_profile_id)    
        query = db.query(SensorData).filter(*filter).distinct(SensorData.dev_eui).order_by(SensorData.dev_eui, SensorData.time.desc()).offset(skip).limit(limit)

        return query
    except SQLAlchemyError:
        return []


# Service for Endpoint to get all devices history with pagination

def get_devices_history(db: Session, dev_eui: Optional[str], application_id: Optional[str], device_profile_id: Optional[str], skip: int = 0, limit: int = 10):
    try:
        filter = [SensorData.object != '{}']
        if dev_eui:
            filter.append(SensorData.dev_eui == dev_eui)
        if application_id:
            filter.append(SensorData.application_id == application_id)
        if device_profile_id:
            filter.append(SensorData.device_profile_id == device_profile_id)    
        query = db.query(SensorData).filter(*filter).order_by(SensorData.dev_eui, SensorData.time.desc()).offset(skip).limit(limit)

        return query
    except SQLAlchemyError:
        return []