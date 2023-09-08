from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class UserRole(str, Enum):
    admin = "admin"
    student = "student"


class UserBase(BaseModel):
    email: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=50)


class UserLogin(UserBase):
    ...


class UserCreate(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    internal_role: UserRole = Field(UserRole.student, min_length=1, max_length=50)


class UserUpdate(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    internal_role: UserRole = Field(..., min_length=1, max_length=50)


class UserDto(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., min_length=1, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    internal_role: UserRole = Field(..., min_length=1, max_length=50)
