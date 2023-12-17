#! /bin/bash
echo "ruff check --diff fastapi_dramatiq/"
ruff check --diff fastapi_dramatiq/
echo "DONE!"
echo "ruff format --diff fastapi_dramatiq/"
ruff format --diff fastapi_dramatiq/
echo "DONE!"
echo "mypy fastapi_dramatiq/"
mypy fastapi_dramatiq/
echo "DONE!"
