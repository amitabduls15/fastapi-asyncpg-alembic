from fastapi import Depends
from sqlmodel import select, update
from sqlmodel.ext.asyncio.session import AsyncSession

from db.db import get_session
from repository.user.models import User


async def select_all_users(session: AsyncSession = Depends(get_session)):
    statement = select(User)
    res = await session.execute(statement)
    return res.scalars().all()


async def find_user(name, session: AsyncSession = Depends(get_session)):
    statement = select(User).where(User.username == name)
    res = await session.execute(statement)
    user = res.first()

    return user


async def update_password_user(user_id, new_password, session: AsyncSession = Depends(get_session)):
    statement = select(User).where(User.user_id == user_id)
    res = await session.execute(statement)
    user = res.one()[0]
    user.password = new_password
    session.add(user)
    await session.commit()

    return user
