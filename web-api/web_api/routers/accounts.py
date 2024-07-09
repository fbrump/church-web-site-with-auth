from datetime import timedelta
from typing import Annotated
from uuid import UUID

import repository
import schemas
from dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from middlewares.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    Scope,
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_current_active_user,
    get_password_hash,
    oauth2_scheme,
)
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


def check_scopes(user_scopes: list[str], form_scopes: list[str]) -> bool:
    have_permission = True
    for item in form_scopes:
        if not item in user_scopes:
            have_permission = False
    return have_permission


@router.post(
    "/token",
    summary="Create access and refresh tokens for user",
    response_model=schemas.Token,
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> schemas.Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif (
        not user.client_id == form_data.client_id
        and not user.client_secret == form_data.client_secret
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect client (id or secret)",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif not check_scopes(user.scopes, form_data.scopes):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect scopes",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {
        "name": user.full_name,
        "email": user.email,
        "scopes": user.scopes,
    }
    access_token = create_access_token(
        user.username,
        data=data,
        expires_delta=access_token_expires,
    )
    refresh_token = create_refresh_token(
        user.username,
        data=data,
        expires_delta=access_token_expires,
    )
    return schemas.Token(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )


@router.post("/register/", summary="Create a new user", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400)
    schema_user = schemas.UserInDB(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        email=user.email,
        full_name=user.full_name,
        disabled=user.disabled,
        client_id=user.client_id,
        client_secret=user.client_secret,
        scopes=user.scopes
    )
    return repository.create_user(db=db, user=schema_user)


@router.get(
    "/users/me/",
    summary="Get details of currently logged in user",
    response_model=schemas.User,
)
async def read_users_me(
    current_user: Annotated[
        schemas.User, Security(get_current_active_user, scopes=[Scope.ACCOUNT_READ])
    ]
):
    return current_user


@router.post("/logout/")
async def logout_revoke_token(
    current_user: Annotated[
        schemas.User, Security(get_current_active_user, scopes=[Scope.ACCOUNT_READ])
    ],
):
    oauth2_scheme.revoke_token()
    return {"message": "Token revoked"}


@router.put(
    "/users/{username}/scopes/",
    summary="Update user scopes",
    response_model=schemas.UserScopeBase,
)
async def update_user_scopes(
    username: str,
    scopes: schemas.UserScopeUpdate,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(get_db),
) -> schemas.UserScope:
    db_user = repository.get_user_by_username(db, username=current_user.username)
    if not db_user:
        raise HTTPException(status_code=400)
    elif not db_user.username == username:
        raise HTTPException(status_code=400)
    schema_user_scopes = schemas.UserScope(user_id=db_user.id, scopes=scopes.scopes)
    return repository.update_user_scopes(db=db, user_scopes=schema_user_scopes)
