poetry run python3 -m fastapi_dramatiq.main

# Overriding the .env settings
# poetry run uvicorn fastapi_dramatiq.main:app --host 0.0.0.0 --port 5000 --reload --log-config log_config.yml
