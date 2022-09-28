from configs.database import DatabaseConfig
from configs.application import ApplicationConfig
from pkg.env import Env

databaseConfig = DatabaseConfig()
applicationConfig = ApplicationConfig()

env: Env


def init(env_file: str):
    global env
    env = Env(env_file)
    databaseConfig.load(env)
    applicationConfig.load(env)


init('.env')
