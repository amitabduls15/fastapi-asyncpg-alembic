from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from datasource.db.async_pg import get_session
from repository.history_login.models import HistoryLogin
from repository.repository_abstract import RepositoryAbstract


class RepositoryHistoryLogin(RepositoryAbstract):
    pass


repository_history_login = RepositoryHistoryLogin(HistoryLogin)
