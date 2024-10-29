from fastapi import FastAPI
from .config import Config
from .api import devices
from .models import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
def create_app() -> FastAPI:
	app = FastAPI(
		title="Chirpstack PostgreSQL integration API",
		description="Middleware between future apps and chirp integration db",
		version="1.0.0",
		openapi_tags=[
			{
				"name": "Sensor data",
				"description": "Perform queries on event_up table",
			}
		]
	)

	app.include_router(devices.router)
	return app

app = create_app()

