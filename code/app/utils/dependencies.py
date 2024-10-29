from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from ..config import config
from ..models import SessionLocal

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_token(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header != config.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )
    return api_key_header

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
