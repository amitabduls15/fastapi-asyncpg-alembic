from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import configs

config_name = '.env'
configs.init(config_name)

from configs import applicationConfig

from deliveries.auth import auth_router
from datasource.db.async_pg import init_db

app = FastAPI()

origins = [
    f"http://{applicationConfig.host}:{applicationConfig.port}",
    f"https://{applicationConfig.host}:{applicationConfig.port}",
    applicationConfig.domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix='/auth')


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host=applicationConfig.host, port=applicationConfig.port, reload=True)
