import multiprocessing
from typing import List

from pkg.env import Env


class DatabaseConfig:
    _type: str
    _host: str
    _database: str
    _user: str
    _password: str
    _port: str
    _url: str

    @property
    def type(self) -> str:
        return self._type

    @property
    def host(self) -> str:
        return self._host

    @property
    def database(self) -> str:
        return self._database

    @property
    def user(self) -> str:
        return self._user

    @property
    def password(self) -> str:
        return self._user

    @property
    def url(self) -> str:
        return self._url

    @classmethod
    def load(cls, env: Env):
        cls._type = env.get_str("TYPE_DB", default='postgresql+psycopg2')
        cls._host = env.get_str("HOST_DB", default='localhost')
        cls._database = env.get_str("DATABASE", default='postgres')
        cls._user = env.get_str("USER_DB", default='postgres')
        cls._password = env.get_str("PASSWORD_DB", default='')
        cls._port = env.get_str("PORT_DB", default='5432')
        cls._url = f'{cls._type}://{cls._user}:{cls._password}@{cls._host}:{cls._port}/{cls._database}'
