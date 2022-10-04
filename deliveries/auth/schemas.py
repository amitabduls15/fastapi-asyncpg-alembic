import datetime

from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    username: str
    password: str = Field(max_length=256, min_length=6)


class UserInputSchema(UserLoginSchema):
    password2: str
    email: EmailStr
    role_id: int

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords don\'t match')
        return v


class UserData(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    created_at: datetime.datetime
    role_id: int


class UserChangePasswordInputSchema(BaseModel):
    new_password: str = Field(max_length=256, min_length=6)
    confirm_password: str

    @validator('confirm_password')
    def password_match(cls, v, values, **kwargs):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('passwords don\'t match')
        return v


class UserChangePassword(UserChangePasswordInputSchema):
    user_id = int
