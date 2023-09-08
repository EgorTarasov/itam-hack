from fastapi import APIRouter
from src.user.views import auth_router

views_router = APIRouter()

views_router.include_router(auth_router)
