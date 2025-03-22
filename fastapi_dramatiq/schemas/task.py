from typing import Union

from pydantic import BaseModel, ConfigDict, Field

BASE_SCHEMA_EXTRA = {"example": {"seconds": 10}}


class TaskCreate(BaseModel):
    seconds: int = Field(
        title="Duration in seconds the task should run for.", ge=1, le=300
    )

    model_config = ConfigDict(json_schema_extra=dict(**BASE_SCHEMA_EXTRA))


class Task(BaseModel):
    message_id: Union[str, None] = None
    seconds: int
    status: str
