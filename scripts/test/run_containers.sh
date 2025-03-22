#!/bin/bash

# Check if any arguments are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <commands>"
    echo "Example: $0 up service1 down service2"
    exit 1
fi

DOCKER_COMPOSE_FILE="docker-compose.yaml"

# Initialize an array to store the commands
commands=()

# Loop through the provided arguments and add them to the commands array
for arg in "$@"; do
    commands+=("$arg")
done

docker compose -f $DOCKER_COMPOSE_FILE --env-file .env "${commands[@]}"
