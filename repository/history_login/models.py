import datetime
from typing import Optional, List

from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship, Column, String

from repository.user.models import User


class HistoryLogin(SQLModel, table=True):
    __tablename__ = 'history_login'
    id: Optional[int] = Field(default=None, primary_key=True)
    login_at: datetime.datetime = datetime.datetime.now()
    token: str = Field(max_length=300, min_length=1)
    device: str = Field(max_length=256)

    user_id: int = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="HistoryLogin")
