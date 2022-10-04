import datetime
from typing import Optional

from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship, Column, String


class User(SQLModel, table=True):
    # __tablename__ = 'ucok' #uncoment this to use different tablenames than lower classname
    id: Optional[int] = Field(default=None, primary_key=True)  # primary key and auto increment
    username: str = Field(index=True, sa_column=Column("username", String, unique=True))
    password: str = Field(max_length=256, min_length=6)
    email: EmailStr
    created_at: datetime.datetime = datetime.datetime.now()
