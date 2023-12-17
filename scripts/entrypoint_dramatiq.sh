#!/usr/bin/env bash

delay=1
while true; do
  poetry run dramatiq fastapi_dramatiq.actors
  if [ $? -eq 3 ]; then
    echo "Connection error encountered on startup. Retrying in $delay second(s)..."
    sleep $delay
    delay=$(delay)
  else
    exit $?
  fi
done
