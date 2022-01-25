# Python
from datetime import date
from typing import Optional
from uuid import UUID

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
        min_length=8
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
    pass


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
