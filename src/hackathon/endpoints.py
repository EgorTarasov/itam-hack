from fastapi import APIRouter
from src.data import Base


router = APIRouter(prefix="/hackathon", tags=["hackathon"])


@router.get("/")
async def hack():
    return {"baseId": id(Base)}
