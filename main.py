# Python
from dataclasses import field
from datetime import date, datetime
from typing import Optional
from uuid import UUID
import uuid
from venv import create

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# FastAPI
from fastapi import FastAPI

app = FastAPI()


# Models

class UserBase(BaseModel):
    user_id: UUID = Field(
        ...
    )
    email: EmailStr = Field(
        ...
    )
class UserLogin(UserBase):
    """
    User Login

    Model to return when the suer logs in
    """
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

    username: str = Field(
        ...
    )


class Tweet(BaseModel):
    tweet_id:uuid = Field(...)
    content:str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
