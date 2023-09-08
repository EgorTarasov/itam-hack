from fastapi import Depends, HTTPException, Cookie, status
from src.auth.jwt import decode_jwt
from src.data.sql import SQLManager
from src.user.domain import UserDto
from src.user.repository import UserRepository
from src.utils.logging import get_logger


async def get_db() -> SQLManager:
    """Get the database connection"""
    return SQLManager(get_logger("db"))


async def get_user_repository(db: SQLManager = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


async def get_current_user(
    access_token: str | None = Cookie(None),
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserDto | None:

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated (current_user)",
        )
    user_id = decode_jwt(access_token)
    return user_repository.get(user_id=user_id)
