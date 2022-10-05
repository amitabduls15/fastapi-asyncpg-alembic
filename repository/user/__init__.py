import datetime

from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from datasource.db.async_pg import get_session
from repository.user.models import User

from repository.repository_abstract import RepositoryAbstract


class RepositoryUser(RepositoryAbstract):
    async def find_by_username(self, username: str, session: AsyncSession = Depends(get_session)):
        statement = select(self.model).where(self.model.username == username)
        res = await session.execute(statement)
        user = res.first()

        return user

    async def update_password(self, user_id, new_hash_pwd, session: AsyncSession = Depends(get_session)):
        statement = select(self.model).where(self.model.id == user_id)
        res = await session.execute(statement)
        user = res.one()[0]
        user.hash_pw = new_hash_pwd
        user.update_at = datetime.datetime.utcnow()
        session.add(user)
        await session.commit()

        return user


repository_user = RepositoryUser(User)

# async def select_all_users(session: AsyncSession = Depends(get_session)):
#     statement = select(User)
#     res = await session.execute(statement)
#     return res.scalars().all()
#
#
# async def insert_user(new_user: User, session: AsyncSession = Depends(get_session)):
#     u = User(username=new_user.username, hash_pw=new_user.hash_pw,
#              email=new_user.email, role_id=new_user.role_id)
#     session.add(u)
#     await session.commit()
#
#
# async def find_user(username: str, session: AsyncSession = Depends(get_session)):
#     statement = select(User).where(User.username == username)
#     res = await session.execute(statement)
#     user = res.first()
#
#     return user
