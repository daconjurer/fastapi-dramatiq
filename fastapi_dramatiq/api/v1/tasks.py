from fastapi import APIRouter

from fastapi_dramatiq import schemas
from fastapi_dramatiq.actors.task import run_task


router = APIRouter()


@router.post("", response_model=schemas.Task)
def create_task(task_in: schemas.TaskCreate):
    message_id = None
    status = "failed"
    # if ran without send() message_id will not be present
    try:
        task = run_task.send(seconds=task_in.seconds)
        message_id = task.message_id
        status = "submitted"
    except Exception as e:
        # Only hit once the actor has exceeded the max retries
        raise e

    return schemas.Task(message_id=message_id, seconds=task_in.seconds, status=status)
