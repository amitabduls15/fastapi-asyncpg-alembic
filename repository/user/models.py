import datetime
from typing import Optional, List

from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship, Column, String

from repository.reff_role.models import ReffRole


class User(SQLModel, table=True):
    # __tablename__ = 'ucok' #uncoment this to use different tablenames than lower classname
    id: Optional[int] = Field(default=None, primary_key=True)  # primary key and auto increment
    username: str = Field(index=True, sa_column=Column("username", String, unique=True))
    hash_pw: str = Field(max_length=256, min_length=6)
    email: EmailStr
    created_at: datetime.datetime = datetime.datetime.now()
    update_at: Optional[datetime.datetime] = Field(nullable=True)

    role_id: int = Field(nullable=False, foreign_key="reff_role.id")
    role: Optional[ReffRole] = Relationship(back_populates="Users")
