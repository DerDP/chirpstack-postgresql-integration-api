from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from uuid import UUID

class SensorDataSchema(BaseModel):
    dev_eui: str
    application_id: UUID
    device_profile_id: UUID
    time: datetime
    object: Any

    class Config:
        from_attributes = True
