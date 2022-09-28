import multiprocessing
from typing import List

from pkg.env import Env


class ApplicationConfig:
    _secretkey: str
    _port: int
    _host: str

    @property
    def secretkey(self) -> str:
        return self._secretkey

    @property
    def port(self) -> int:
        return self._port

    @property
    def host(self) -> str:
        return self._host

    @classmethod
    def load(cls, env: Env):
        cls._secretkey = env.get_str("SECRET_KEY", default='.dev')
        cls._port = env.get_int("PORT", default=5000)
        cls._host = env.get_str("HOST", default='localhost')
