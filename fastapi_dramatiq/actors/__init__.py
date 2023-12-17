import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from fastapi_dramatiq.settings.application import get_app_settings

settings = get_app_settings()


def get_broker_url(containerized: bool = False) -> str:
    """
    Returns the URL to connect to the RabbitMQ message broker.

    If the API is running in a container within the same network as the message broker,
    the RABBITMQ_HOST variable must be the name of the RabbitMQ container and the port
    must be 5672/5671 (depending on TLS settings).

    If the API is running directly on the host, the RABBITMQ_HOST variable must be
    localhost and the port must be the port on which RabbitMQ's port is mapped
    (RABBITMQ_MAPPED_PORT).

    Update accordingly in the .env file.

    Returns:
        str: _description_
    """
    host = "localhost"
    port = settings.docker.docker_rabbitmq_mapped_port

    if containerized:
        host = settings.rabbitmq.rabbitmq_host
        port = 5672

    return (
        f"amqp://{settings.rabbitmq.rabbitmq_user}:{settings.rabbitmq.rabbitmq_password}"
        f"@{host}:{port}/{settings.rabbitmq.rabbitmq_vhost}"
    )


rabbitmq_broker = RabbitmqBroker(url=get_broker_url(settings.containerized))
dramatiq.set_broker(rabbitmq_broker)


from fastapi_dramatiq.actors.task import run_task, count_words  # noqa: E402

__all__ = ("run_task", "count_words")
