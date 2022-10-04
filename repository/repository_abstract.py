from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from datasource.db.async_pg import get_session


class RepositoryAbstract:
    def __init__(self, model):
        self.model = model

    async def select_all(self, session: AsyncSession = Depends(get_session)):
        statement = select(self.model)
        res = await session.execute(statement)
        return res.scalars().all()

    async def find_by_id(self, id_, session: AsyncSession = Depends(get_session)):
        statement = select(self.model).where(self.model.id == id_)
        res = await session.execute(statement)
        res_first = res.first()

        return res_first

    async def delete_by_id(self, id_, session: AsyncSession = Depends(get_session)):
        data = await self.find_by_id(id_, session)
        await session.delete(data)
        await session.commit()

    @staticmethod
    async def insert_one(data, session: AsyncSession = Depends(get_session)):
        session.add(data)
        await session.commit()

    @staticmethod
    async def insert_many(list_data: list, session: AsyncSession = Depends(get_session)):
        for data in list_data:
            session.add(data)
        await session.commit()
