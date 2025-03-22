# syntax = docker/dockerfile:1.2

# Build argument for Python version
ARG PYTHON_VERSION=3.12

# Platform args for multi-arch builds
ARG TARGETPLATFORM=linux/amd64

FROM --platform=$TARGETPLATFORM python:${PYTHON_VERSION}-slim as python-base

# Builder stage
FROM python-base as builder

ARG POETRY_VERSION=2.0.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY fastapi_dramatiq ./fastapi_dramatiq
RUN pip install poetry==${POETRY_VERSION} && \
    touch README.md && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev

ENV PATH="/app/.venv/bin:$PATH"

FROM builder as api

COPY log_config.yml .env ./
CMD ["python3", "-m", "fastapi_dramatiq.main"]

FROM builder as workers

ADD .env /app/.env
ADD scripts/entrypoint_dramatiq.sh /app/entrypoint_dramatiq.sh
