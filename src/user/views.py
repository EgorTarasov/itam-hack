from fastapi import APIRouter, Request
from src.utils import templates

auth_router = APIRouter()


@auth_router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})
