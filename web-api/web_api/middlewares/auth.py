import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, Union

import jwt
import repository
import schemas
from dependencies import get_db
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.orm import Session

JWT_SECRET_KEY = os.environ.get(
    "JWT_SECRET_KEY", "3409eedfe8abc39c02a5ce80816b4dca22832b5976fffc0af215efb104f69a88"
)
JWT_REFRESH_SECRET_KEY = os.environ.get(
    "JWT_REFRESH_SECRET_KEY",
    "a97f878ec9b3d63e9e67054d9da4147d7c6bfd849f74e2a14b420008f9c20d77",
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Scope:
    ACCOUNT_READ = "account:read"
    ACCOUNT_WRITE = "account:write"
    SMALL_GROUP_READ = "small-group:read"
    SMALL_GROUP_WRITE = "small-group:write"
    ADDRESS_READ = "address:read"


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/accounts/token",
    scopes={
        Scope.ACCOUNT_READ: "Read information of the current user.",
        Scope.ACCOUNT_WRITE: "Register or update a new user.",
        Scope.SMALL_GROUP_READ: "Read small groups information.",
        Scope.SMALL_GROUP_WRITE: "Register or update small group.",
        Scope.ADDRESS_READ: "Read addresses information.",
    },
)


def verify_password(
    plain_password: Union[str, bytes], hashed_password: Union[str, bytes, Any]
) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: Union[str, bytes]) -> str:
    return pwd_context.hash(password)


def authenticate_user(
    db: Session, username: str, password: str
) -> Union[schemas.User, bool]:
    user = repository.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return schemas.User.mapper(user)


def create_access_token(
    subject: Union[str, Any], data: dict, expires_delta: timedelta | None = None
) -> Any:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": str(subject)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(
    subject: Union[str, Any], data: dict, expires_delta: int = None
) -> str:
    to_encode = data.copy()
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expires_delta, "sub": str(subject)})
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
) -> schemas.User:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = schemas.TokenData(username=username, scopes=token_scopes)
    except (InvalidTokenError, ValidationError):
        raise credentials_exception
    user = repository.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return schemas.User.mapper(user)


async def get_current_active_user(
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.ACCOUNT_READ])
    ],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
