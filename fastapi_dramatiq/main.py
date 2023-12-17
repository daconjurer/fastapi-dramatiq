from fastapi_dramatiq.core.app_factory import create_app

from fastapi_dramatiq.settings.application import get_app_settings

settings = get_app_settings()

app = create_app()

if __name__ == "__main__":
    import uvicorn

    _reload = settings.environment == "dev"

    uvicorn.run(
        app="fastapi_dramatiq.main:app",
        host=str(settings.api.api_host),
        port=settings.api.api_port,
        reload=_reload,
        log_config="log_config.yml",
    )
