from typing import Union
from uuid import UUID

import models
import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select, delete


def get_small_group(db: Session, small_group_id: UUID) -> models.SmallGroup:
    return db.scalar(select(models.SmallGroup).where(models.SmallGroup.id==small_group_id))


def get_small_groups(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.scalars(select(models.SmallGroup)
        .where(models.SmallGroup.is_active == True)
        .offset(skip)
        .limit(limit))
    )


def create_small_group(db: Session, small_group: schemas.SmallGroupCreate) -> schemas.SmallGroup:
    db_small_group = models.SmallGroup(
        title=small_group.title,
        weekday=small_group.weekday,
        start_at=small_group.start_at,
        finish_at=small_group.finish_at,
    )
    db_address = models.Address(
        street=small_group.address.street,
        reference=small_group.address.reference,
        number=small_group.address.number,
        zip_code=small_group.address.zip_code,
        neighborhood=small_group.address.neighborhood,
        city=small_group.address.city,
        state=small_group.address.state,
        country=small_group.address.country,
        small_group=db_small_group,
    )
    db.add_all([db_small_group, db_address])
    db.commit()
    return db_small_group


def get_small_group_by_title(db: Session, title: str) -> models.SmallGroup:
    return db.scalar(select(models.SmallGroup).where(models.SmallGroup.title == title))


def get_address_by_small_group(db: Session, small_group_id: UUID) -> models.Address:
    return (
        db.scalar(select(models.Address)
        .where(models.Address.small_group_id == small_group_id))
    )


def get_address_by_id(db: Session, address_id: int) -> models.Address:
    return db.scalar(select(models.Address).where(models.Address.id==address_id))


def get_contact_phones_by_small_group(db: Session, small_group_id: int):
    return (
        db.scalars(select(models.ContactPhone)
        .where(models.ContactPhone.small_group_id == small_group_id))
    )


def get_user_by_username(db: Session, username: str) -> models.User:
    return db.scalar(select(models.User).where(models.User.username == username))


def get_user_by_token(db: Session, token: str) -> models.User:
    return db.scalar(select(models.User).where(models.User.hashed_password == token))


def create_user(db: Session, user: schemas.UserInDB) -> schemas.User:
    if user.scopes:
        db_scopes = [models.UserScope(scope=models.ScopeEnum(scope)) for scope in user.scopes]
    else:
        db_scopes = []
    db_user = models.User(
        username=user.username,
        hashed_password=user.hashed_password,
        email=user.email,
        full_name=user.full_name,
        disabled=user.disabled,
        client_id=user.client_id,
        client_secret=user.client_secret,
        scopes=db_scopes
    )
    db.add(db_user)
    db.commit()
    return schemas.User.mapper(db_user)


def get_token(db: Session, token: str) -> models.Token:
    return db.scalar(select(models.Token).where(models.Token.token == token))


def create_token(db: Session, token: str, user_id: int) -> models.Token:
    db_token = models.Token(token=token, user_id=user_id)
    db.add(db_token)
    db.commit()
    return db_token

def update_user_scopes(
    db: Session, user_scopes: schemas.UserScope
) -> schemas.UserScope:
    db.execute(delete(models.UserScope).where(
        models.UserScope.user_id == user_scopes.user_id
    ))
    db.flush()
    user_scopes_to_add = []
    if user_scopes.scopes:
        for scope in user_scopes.scopes:
            user_scopes_to_add.append(
                models.UserScope(
                    user_id=user_scopes.user_id, scope=models.ScopeEnum(scope)
                )
            )
        db.add_all(user_scopes_to_add)
    db.commit()
    return user_scopes
