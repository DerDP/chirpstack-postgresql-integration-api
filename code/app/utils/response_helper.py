from typing import List
from ..models.sensor_data import SensorData

def build_response(sensor_data: List[SensorData], total_count: int, skip: int, limit: int) -> dict:
    return {
        "total_count": total_count,
        "limit": limit,
        "offset": skip,
        "devices": [
            {
                'device_name': data.device_name,
                'dev_eui': data.dev_eui,
                'application_id': data.application_id,
                'device_profile_id': data.device_profile_id,
                'time': data.time,
                'object': data.object
            }
            for data in sensor_data
        ]
    }
