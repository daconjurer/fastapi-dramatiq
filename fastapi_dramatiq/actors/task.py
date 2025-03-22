import time

import dramatiq
import requests
from loguru import logger


@dramatiq.actor
def run_task(seconds: int):
    logger.info("task recevied!")
    for x in range(seconds, 0, -1):
        logger.info(f"counting down until task complete - seconds: {x}")
        time.sleep(1)
    logger.info("task completed!")


@dramatiq.actor
def count_words(url: str):
    logger.info("task recevied!")
    response = requests.get(url)
    count = len(response.text.split(" "))
    logger.info(f"There are {count} words at {url!r}.")
    logger.info("task completed!")
