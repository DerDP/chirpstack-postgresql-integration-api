from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.sensor_data import SensorData
from typing import Optional


# Service for Endpoint to get all devices with pagination


def get_devices(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(SensorData).order_by(SensorData.time.desc()).filter(SensorData.object != '{}').offset(skip).limit(limit).all()
    except SQLAlchemyError:
        return []


# Endpoint to get all rows for devices matching a specific dev_eui


def get_device_by_dev_eui(db: Session, dev_eui: str, skip: int = 0, limit: int = 10):
    try:
        return db.query(SensorData).filter(SensorData.dev_eui == dev_eui).filter(SensorData.object != '{}').offset(skip).limit(limit).all()
    except SQLAlchemyError:
        return []
    
    
# Service for Endpoint to get devices by application ID, with optional filters    
    
def get_device_by_dev_applicationID(db: Session, application_id: str, dev_eui: Optional[str], device_profile_id: Optional[str], skip: int = 0, limit: int = 10):
    try:
        query = db.query(SensorData).filter(SensorData.application_id == application_id).filter(SensorData.object != '{}')
        
        if dev_eui:
            query = query.filter(SensorData.dev_eui == dev_eui)
        if device_profile_id:
            query = query.filter(SensorData.device_profile_id == device_profile_id) 

        return query.offset(skip).limit(limit).all()
    except SQLAlchemyError:
        return []    
    
    
# Service for Endpoint to get devices by device profile ID    

def get_device_by_dev_profileID(db: Session, device_profile_id: str,  dev_eui: Optional[str], application_id: Optional[str],  skip: int = 0, limit: int = 10):
    try:
        query = db.query(SensorData).filter(SensorData.device_profile_id == device_profile_id).filter(SensorData.object != '{}')
        
        if dev_eui:
            query = query.filter(SensorData.dev_eui == dev_eui)
        if application_id:
            query = query.filter(SensorData.application_id == application_id) 

        return query.offset(skip).limit(limit).all()
    except SQLAlchemyError:
        return []    