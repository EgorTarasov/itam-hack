from fastapi import FastAPI
from src.api.api import api_router
from src.views import views_router


def create_app():
    _app = FastAPI(
        name="Itam Hacks",
        description="Itam Hacks API",
    )
    _app.include_router(api_router)
    _app.include_router(views_router)
    return _app
