from fastapi import APIRouter, Depends, Response, HTTPException, status, Cookie, Request
from src.data.dependecies import get_user_repository, get_current_user
from src.user.domain import UserLogin, UserCreate, UserDto
from src.user.repository import UserRepository
from src.auth.jwt import (
    create_access_jwt,
    verify_password,
    get_password_hash,
    decode_jwt,
)
from src.utils.logging import get_logger
from src.utils.settings import settings

router = APIRouter(prefix="/users", tags=["users"])


log = get_logger(__name__)


@router.post("/login")
async def login(
    response: Response,
    user_data: UserLogin,
    repository: UserRepository = Depends(get_user_repository),
):
    try:
        user = repository.get(email=user_data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        if not verify_password(user_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        response.set_cookie(
            "access_token",
            create_access_jwt(user.id),
            max_age=60 * 60 * 24,
            path="*",
        )
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@router.post("/signup")
async def signup(
    response: Response,
    user_data: UserCreate,
    repository: UserRepository = Depends(get_user_repository),
):
    try:
        hashed_password = get_password_hash(user_data.password)
        user_data.password = hashed_password
        user = repository.add(user_data)
        response.set_cookie(
            "access_token",
            create_access_jwt(user.id),
            # max_age=
            path="*",
        )
        response.status_code = status.HTTP_201_CREATED
        return response
    except Exception as e:
        log.warning(str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    response.status_code = status.HTTP_204_NO_CONTENT
    return response


@router.get("/me")
async def me(
    current_user: UserDto = Depends(get_current_user),
):
    return current_user
