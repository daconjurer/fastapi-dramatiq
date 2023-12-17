from pydantic import Field, IPvAnyAddress

from fastapi_dramatiq.settings.base import CommonSettings


class APISettings(CommonSettings):
    api_host: str = Field(validation_alias="API_HOST", default="0.0.0.0")
    api_port: int = Field(validation_alias="API_PORT", default=3000)
