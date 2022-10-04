from fastapi import APIRouter, HTTPException, Depends, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED

from deliveries.auth.controller import AuthHandler
from deliveries.auth.schemas import *
from sqlalchemy.ext.asyncio import AsyncSession

from datasource.db.async_pg import get_session
from repository.history_login import repository_history_login, HistoryLogin
from repository.user.models import User
from repository.user import repository_user
from repository.reff_role import repository_reff_role

auth_router = APIRouter()
auth_handler = AuthHandler()


@auth_router.post('/registration', status_code=201, tags=['users'],
                  description='Register new user')
async def register(user: UserInputSchema, session: AsyncSession = Depends(get_session)):
    users = await repository_user.select_all(session)
    if any(x.username == user.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hash_pw = auth_handler.get_password_hash(user.password)
    role_res = await repository_reff_role.find_by_id(user.role_id, session)
    if role_res:
        await repository_user.insert_one(User(username=user.username, hash_pw=hash_pw,
                                              role_id=user.role_id, email=user.email), session)
        return JSONResponse(status_code=HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=404, detail='role id is not available')


@auth_router.post('/login', tags=['users'])
async def login(user: UserLoginSchema, request: Request, session: AsyncSession = Depends(get_session)):
    user_agent = request.headers['user-agent']
    user_found = await repository_user.find_by_username(user.username, session)
    if not user_found:
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    user_found = user_found[0]
    verified = auth_handler.verify_password(user.password, user_found.hash_pw)
    if not verified:
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user_found.username)
    new_history = HistoryLogin(user_id=user_found.id, token=token, device=user_agent)
    await repository_history_login.insert_one(new_history, session)
    return {'token': token}


@auth_router.get('/users/me', tags=['users'])
def get_current_user(user_data: UserData = Depends(auth_handler.get_current_user)):
    return user_data


@auth_router.patch('/users/change/password', tags=['users'])
async def get_current_user(user_change_password_input: UserChangePasswordInputSchema,
                           user_data: UserData = Depends(auth_handler.get_current_user),
                           session: AsyncSession = Depends(get_session)):
    hashed_pwd = auth_handler.get_password_hash(user_change_password_input.new_password)

    res = await repository_user.update_password(user_id=user_data.user_id, new_password=hashed_pwd, session=session)
    return user_data
