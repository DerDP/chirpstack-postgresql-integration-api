from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from ..utils.dependencies import verify_token, get_db
from ..schemas.sensor_data_schema import SensorDataSchema
from ..services.device_service import get_devices, get_devices_history
from ..utils.response_helper import build_response
from ..models.sensor_data import SensorData

router = APIRouter()

# Endpoint to get all (unique) devices with pagination
@router.get("/api/devices", response_model=dict, tags=["Sensor data"])
def get_all_unique_devices(
    dev_eui: Optional[str] = Query(None, description="Optional filter by DevEUI"),
    application_id: Optional[str] = Query(None, description="Optional filter by device application ID"),
    device_profile_id: Optional[str] = Query(None, description="Optional filter by device profile ID"),
    limit: int = Query(10),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    db: Session = Depends(get_db),
    token: str = Depends(verify_token),
):
  
    try:
        sensor_data = get_devices(db, dev_eui, application_id, device_profile_id, skip=skip, limit=limit)
        total_count = sensor_data.count()
        return build_response(sensor_data, total_count, skip, limit)
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to get all (unique) devices with pagination
@router.get("/api/devices/history", response_model=dict, tags=["Sensor data history"])
def get_all_unique_devices(
    dev_eui: Optional[str] = Query(None, description="Optional filter by DevEUI"),
    application_id: Optional[str] = Query(None, description="Optional filter by device application ID"),
    device_profile_id: Optional[str] = Query(None, description="Optional filter by device profile ID"),
    limit: int = Query(10),  # Default limit 10, max 100
    skip: int = Query(0),  # Pagination
    db: Session = Depends(get_db),
    token: str = Depends(verify_token),
):
  
    try:
        sensor_data = get_devices_history(db, dev_eui, application_id, device_profile_id, skip=skip, limit=limit)
        total_count = get_devices_history(db, dev_eui, application_id, device_profile_id, skip=None, limit=None).count()
        return build_response(sensor_data, total_count, skip, limit)
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))