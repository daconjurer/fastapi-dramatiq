# Actors need to be defined after the broker settings
from fastapi_dramatiq.actors.task import count_words

from loguru import logger

if __name__ == "__main__":
    # Send a message using the actor
    test_url = "https://www.google.com"
    count_words.send(url=test_url)
    logger.info(f"Sent message: {test_url}")
