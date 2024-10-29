# Introduction 

API Middelware for the PostgreSQL Chirpstack integration.	
Swagger page is available at /docs web path.

## Prerequisites

- Python 3.8+
- Chirpstack with PostgreSQL integration
- Environment setup for the API key and database connection string

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1. Clone the Repository:
   ```bash
   git clone https://github.com/DerDP/chirpstack-postgresql-integration-api
   cd chirp-integration-api/code/app
2.	Install Dependencies:
	```bash
	pip install -r requirements.txt
	```
3.	Set the following environment variables in your environment:
	- `API_KEY`: The API key for access to the endpoints.
	- `DATABASE_URL`: The PostgreSQL connection URL (e.g., `postgresql://user:password@localhost:5432/database_name`).
	- Or Adjust `code/app/.env` file
4.	Database Setup:	 	
	- Ensure that your PostgreSQL database is running and contains the event_up table with a schema matching the `SensorData` model.


# Run locally

From folder `code/` execute:


	uvicorn app.main:app --reload
	

# Run in Docker

You can build the docker image from `code/` folder using the following command:
	

	docker build -t fastapi-chirpstack:latest --no-cache .


To test run docker container, run the following command:

```
docker run -d \
  --name fastapi-chirpstack \
  -e DATABASE_URL="<your_database_url>" \
  -e API_KEY="<your_api_key>" \
  -p 8000:8000 \
  fastapi-chirpstack:latest
```

# k8s deployment
Adjust the deploy.sh in `k8s/` folder and run following commands (populate `code/app/.env` as secret is created with these values):

```bash
chmox +x deploy.sh
./deploy.sh


