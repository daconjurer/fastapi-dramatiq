from pydantic import Field

from fastapi_dramatiq.settings.base import CommonSettings


class DockerSettings(CommonSettings):
    docker_rabbitmq_mapped_port: int = Field(
        validation_alias="DOCKER_RABBITMQ_MAPPED_PORT", default=5500
    )
    docker_rabbitmq_mapped_management_port: int = Field(
        validation_alias="DOCKER_RABBITMQ_MAPPED_MANAGEMENT_PORT", default=15500
    )
    docker_api_mapped_port: int = Field(
        validation_alias="DOCKER_API_MAPPED_PORT", default=3030
    )
