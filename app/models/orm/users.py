from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import EmailStr

from . import USERS_TABLENAME


class User(SQLModel, table=True):
    __tablename__ = USERS_TABLENAME

    id: Optional[UUID] = Field(primary_key=True, description="User ID")
    email: EmailStr = Field(nullable=False, unique=True, description="User's email")
    username: str = Field(nullable=False, unique=True, description="User's username")
    password: str = Field(nullable=False, description="User's password")
    creation_dt: datetime = Field(nullable=False, default=datetime.now(), description="User creation date")
    verified: bool = Field(nullable=False, default=False, description="User's email verified")
    pw_attempts: int = Field(nullable=False, default=0, description="User tentatives to access with wrong credentials")
