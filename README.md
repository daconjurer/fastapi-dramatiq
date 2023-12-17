FastAPI + Dramatiq with RabbitMQ broker
=======================================

A demo app for task queueing using [FastAPI](https://fastapi.tiangolo.com/) and
[Dramatiq](https://dramatiq.io/index.html) with [RabbitMQ](https://www.rabbitmq.com/)
as the broker.

## Configuration
The different settings for the app, broker and workers are defined in the `.env`
file at the root of the project. The settings are then used in the code through
[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).
For further details, see the `fastapi_dramatiq.settings` module.

The settings for running the demo in containers are slightly different compared to
running the API and workers locally. Mainly because of the differences in the
RabbitMQ URL. See the function `get_broker_url()` in the module
`fastapi_dramatiq.actors` for details.

## Usage (local API + workers)

The demo requires a message broker, `Dramatiq` workers and an API. Follow these
steps to test with the API and workers running locally.

#### RabbitMQ test broker
The test broker can be started with a helper script. It uses the Docker image of
`RabbitMQ` and a docker-compose file. Normal Docker flags can be passed to the
script (`-d`, `--build`, etc.) and uses the environment variables defined in the
`.env`` file at the root of the project.

```
./scripts/test/run_containers.sh up rabbitmq
```

#### Dramatiq worker start-up
The worker can be started with the helper script that uses the Dramatiq CLI utility
`dramatiq`. It spawns worker processes to pop the messages off the queue and sending
them to the actor functions (tasks) defined (`fastapi_damatiq.actors.tasks`).

```
./scripts/entrypoint_dramatiq.sh
```

#### API start-up
The API can be started for testing with the `entrypoint_api.sh` script. The
settings are loaded from the `.env` file (any settings with the `API_` prefix).

```
./scripts/entrypoint_api.sh
```

## Usage (Spin up containers)
To run the demo with all 3 components in containers, use the following command:

```
./scripts/test/run_containers.sh up
```

The `run_containers.sh` script accepts Docker/compose arguments, things like
`--build` can be passed as well. The script does not do much more than calling
`docker-compose` with those arguments, using the `docker-compose.yaml` file in
the `docker` folder.

This will spin up 3 containers:
1. rabbitmq
2. tasks_api
3. workers

The first one is based on the offcial RabbitMQ image and uses the `.env` file
settings for RabbitMQ.

The last two are based on the `Dockerfile` in the `docker` directory. Both use the
same base layer as they both use functionality of the package partially. **Changes
in the base layer of that `Dockerfile` might affect both services.**

_________________
_________________

### BONUS: Dramatiq worker example
To see the worker/actor in action or better understand how workers *work*, run the
following command once you have the RabbitMQ broker and Dramatiq workers running
(the `run_containers.sh` script can be used for that).

```
python3 -m examples.example
```

**NOTE:** The settings below are required in the `.env` for the example to work.

```
CONTAINERIZED=False
RABBITMQ_HOST="localhost"
```

It will call the count_words function asynchronously using Dramatiq, as shown in
the [Dramatiq docs](https://dramatiq.io/guide.html).
