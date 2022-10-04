from fastapi import FastAPI
import uvicorn

import configs

config_name = '.env'
configs.init(config_name)

from configs import applicationConfig

from deliveries.auth import auth_router
from datasource.db.async_pg import init_db

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
