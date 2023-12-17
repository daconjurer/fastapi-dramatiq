FROM python:3.10.10-slim-buster as base

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY fastapi_dramatiq ./fastapi_dramatiq
RUN pip install poetry==1.7.0 && \
    touch README.md && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

ENV PATH="/app/.venv/bin:$PATH"


FROM base as api

COPY log_config.yml .env ./
CMD ["python3", "-m", "fastapi_dramatiq.main"]

FROM base as workers

ADD .env /app/.env
ADD scripts/entrypoint_dramatiq.sh /app/entrypoint_dramatiq.sh
