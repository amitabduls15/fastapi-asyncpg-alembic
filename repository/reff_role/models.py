import datetime
from typing import Optional, List

from pydantic import validator, EmailStr
from sqlmodel import SQLModel,Field, Relationship, Column, String


class ReffRole(SQLModel, table=True):
    __tablename__ = 'reff_role'
    id: Optional[int] = Field(default=None, primary_key=True)  # primary key and auto increment
    role: str = Field(max_length=100)


