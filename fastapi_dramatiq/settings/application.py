from functools import lru_cache

from pydantic import Field

from fastapi_dramatiq.settings.api import APISettings
from fastapi_dramatiq.settings.base import CommonSettings
from fastapi_dramatiq.settings.docker import DockerSettings
from fastapi_dramatiq.settings.rabbitmq import RabbitmqSettings


class AppSettings(CommonSettings):
    rabbitmq: RabbitmqSettings = RabbitmqSettings()
    api: APISettings = APISettings()
    docker: DockerSettings = DockerSettings()

    environment: str = Field(validation_alias="ENVIRONMENT", default="dev")
    containerized: bool = Field(validation_alias="CONTAINERIZED", default=False)
    project_name: str = "FastAPI Dramatiq"
    project_description: str = (
        "Demo API to showcase the use of Dramatiq and RabbitMQ to run long "
        "running or CPU intensive tasks in the background of a FastAPI API."
    )


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()
