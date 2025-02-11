from fastapi import FastAPI
from .config import settings
from .api.router import router


def create_app():
    """Create a FastAPI app."""
    config = settings
    app = FastAPI(title=config.app_name)

    app.include_router(router)

    @app.get("/")
    async def root():
        """
        Root endpoint
        """

        return {"message": "Hello World"}

    return app
