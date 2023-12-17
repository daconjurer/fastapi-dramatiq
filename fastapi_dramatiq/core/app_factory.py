from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_dramatiq import __version__
from fastapi_dramatiq.api.v1 import api_router
from fastapi_dramatiq.settings.application import get_app_settings


settings = get_app_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        version=__version__,
        description=settings.project_description,
        docs_url="/",
    )
    register_cors(app)
    register_routers(app)
    return app


def register_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_routers(app: FastAPI) -> None:
    app.include_router(api_router)
