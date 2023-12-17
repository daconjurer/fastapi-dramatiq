from pydantic import Field

from fastapi_dramatiq.settings.base import CommonSettings


class RabbitmqSettings(CommonSettings):
    rabbitmq_user: str = Field(validation_alias="RABBITMQ_USERNAME", default="")
    rabbitmq_password: str = Field(validation_alias="RABBITMQ_PASSWORD", default="")
    rabbitmq_host: str = Field(validation_alias="RABBITMQ_HOST", default="")
    rabbitmq_port: int = Field(validation_alias="RABBITMQ_PORT", default=5672)
    rabbitmq_vhost: str = Field(validation_alias="RABBITMQ_VHOST", default="")
