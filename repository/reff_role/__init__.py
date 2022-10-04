from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from datasource.db.async_pg import get_session
from repository.reff_role.models import ReffRole

from repository.repository_abstract import RepositoryAbstract


class RepositoryReffRole(RepositoryAbstract):
    pass


repository_reff_role = RepositoryReffRole(ReffRole)
