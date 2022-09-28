from fastapi import APIRouter, HTTPException, Security, security, Depends
from fastapi.security import HTTPAuthorizationCredentials
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from api.auth.controller import AuthHandler
from api.auth.schemas import *
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from repository.user.models import User
from repository.user import select_all_users, find_user, update_password_user

auth_router = APIRouter()
auth_handler = AuthHandler()


@auth_router.post('/registration', status_code=201, tags=['users'],
                  description='Register new user')
async def register(user: UserInputSchema, session: AsyncSession = Depends(get_session)):
    users = await select_all_users(session)
    if any(x.username == user.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_pwd = auth_handler.get_password_hash(user.password)
    u = User(username=user.username, password=hashed_pwd, email=user.email)
    session.add(u)
    await session.commit()
    return JSONResponse(status_code=HTTP_201_CREATED)


@auth_router.post('/login', tags=['users'])
async def login(user: UserLoginSchema, session: AsyncSession = Depends(get_session)):
    user_found = await find_user(user.username, session)
    if not user_found:
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    user_found = user_found[0]
    verified = auth_handler.verify_password(user.password, user_found.password)
    if not verified:
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user_found.username)
    return {'token': token}


@auth_router.get('/users/me', tags=['users'])
def get_current_user(user_data: UserData = Depends(auth_handler.get_current_user)):
    return user_data


@auth_router.patch('/users/change/password', tags=['users'])
async def get_current_user(user_change_password_input: UserChangePasswordInputSchema,
                           user_data: UserData = Depends(auth_handler.get_current_user),
                           session: AsyncSession = Depends(get_session)):
    hashed_pwd = auth_handler.get_password_hash(user_change_password_input.new_password)

    res = await update_password_user(user_id=user_data.user_id, new_password=hashed_pwd, session=session)
    return user_data
