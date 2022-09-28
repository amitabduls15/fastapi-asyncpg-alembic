import os
import sys

from fastapi import FastAPI
import uvicorn
import configs

import configs

config_name = '.env'
configs.init(config_name)

from configs import applicationConfig, databaseConfig

from api.auth import auth_router
from db.db import init_db

app = FastAPI()

app.include_router(auth_router)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host=applicationConfig.host, port=applicationConfig.port, reload=True)
