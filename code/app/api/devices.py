from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from ..utils.dependencies import verify_token, get_db
from ..schemas.sensor_data_schema import SensorDataSchema
from ..services.device_service import get_devices, get_device_by_dev_eui, get_device_by_dev_applicationID, get_device_by_dev_profileID
from ..utils.response_helper import build_response
from ..models.sensor_data import SensorData

router = APIRouter()

# Endpoint to get all devices with pagination
@router.get("/api/devices", response_model=dict, tags=["Sensor data"])
def get_all_devices(
    limit: int = Query(10, le=100),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    db: Session = Depends(get_db),
    token: str = Depends(verify_token),
):
  
    try:
        total_count = db.query(SensorData).filter(SensorData.object != '{}').count()
        sensor_data = get_devices(db, skip=skip, limit=limit)
        return build_response(sensor_data, total_count, skip, limit)
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to get all rows for devices matching a specific dev_eui

@router.get("/api/devices/{dev_eui}", response_model=dict, tags=["Sensor data"])
def get_devices_by_dev_eui(
    dev_eui: str,
    limit: int = Query(10, le=100),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    db: Session = Depends(get_db),
    token: str = Depends(verify_token),
):
    try:
        
      total_count = db.query(SensorData).filter(SensorData.object != '{}').filter(SensorData.dev_eui == dev_eui).count()
      sensor_data = get_device_by_dev_eui(db, dev_eui, skip=skip, limit=limit)
      if not sensor_data:
        raise HTTPException(status_code=404, detail="Device not found")
      return build_response(sensor_data, total_count, skip, limit)
  
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))  


# Endpoint to get devices by application ID, with optional filters

@router.get("/api/devices/application/{application_id}", response_model=dict, tags=["Sensor data"])
def get_devices_by_application_id(
    application_id: str,
    dev_eui: Optional[str] = Query(None, description="Optional filter by device EUI within the specified application ID."),
    device_profile_id: Optional[str] = Query(None, description="Optional filter by device profile ID within the specified application ID."),
    limit: int = Query(10, le=100),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    token: str = Depends(verify_token),
    db: Session = Depends(get_db)
):
    try:
        
       total_count = db.query(SensorData).filter(SensorData.object != '{}').filter(SensorData.application_id == application_id).count()
       sensor_data = get_device_by_dev_applicationID(db, application_id, dev_eui, device_profile_id, skip, limit)
       
       if not sensor_data:
           raise HTTPException(status_code=404, detail="Device not found")
       return build_response(sensor_data, total_count, skip, limit)
   
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str("Make sure that {application_id} is a valid Application ID"))
    
    
# Endpoint to get devices by device profile ID
@router.get("/api/devices/profile/{device_profile_id}", response_model=dict, tags=["Sensor data"])
def get_devices_by_device_profile_id(
    device_profile_id: str,
    dev_eui: Optional[str] = Query(None, description="Optional filter by device EUI within the specified profile ID."),
    application_id: Optional[str] = Query(None, description="Optional filter by device application ID within the specified profile ID."),
    limit: int = Query(10, le=100),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    token: str = Depends(verify_token),
    db: Session = Depends(get_db)
):
    try:
        
        total_count = db.query(SensorData).filter(SensorData.object != '{}').filter(SensorData.device_profile_id == device_profile_id).count()
        sensor_data = get_device_by_dev_profileID(db, device_profile_id, dev_eui, application_id, skip, limit)
        
        if not sensor_data:
            raise HTTPException(
                status_code=404, 
                detail=f"No devices found matching the provided device profile ID '{device_profile_id}'."
            )

        return build_response(sensor_data, total_count, skip, limit)

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str("Make sure that {device_profile_id} is a valid device profile id"))    