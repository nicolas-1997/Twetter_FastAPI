# Python
from dataclasses import field
from datetime import date, datetime
from email.policy import HTTP
from importlib.resources import path
from typing import List, Optional
from uuid import UUID
import uuid
from venv import create

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# FastAPI
from fastapi import FastAPI, status

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


# Path Operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

## Users

@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def singup():
    """
    Sing Up

    Register a User
    """
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a Users",
    tags=["Users"]
)
def update_a_user():
    pass

