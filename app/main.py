from fastapi import FastAPI

from app.routes.api import router as api_router
from app.services import create_database
from app.core.config import API_PREFIX


def get_application() -> FastAPI:
    application = FastAPI()

    create_database()

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
