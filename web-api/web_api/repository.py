from typing import Union
from uuid import UUID

import models
import schemas
from sqlalchemy.orm import Session


def get_small_group(db: Session, small_group_id: UUID):
    return db.query(models.SmallGroup).get(small_group_id)


def get_small_groups(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.SmallGroup)
        .filter(models.SmallGroup.is_active == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_small_group(db: Session, small_group: schemas.SmallGroupCreate):
    db_small_group = models.SmallGroup(
        title=small_group.title,
        weekday=small_group.weekday,
        start_at=small_group.start_at,
        finish_at=small_group.finish_at,
    )
    db.add(db_small_group)
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
    db.add(db_address)
    db.commit()
    db.refresh(db_small_group)
    return db_small_group


def get_small_group_by_title(db: Session, title: str):
    return db.query(models.SmallGroup).filter(models.SmallGroup.title == title).first()


def get_address_by_small_group(db: Session, small_group_id: UUID):
    return (
        db.query(models.Address)
        .filter(models.Address.small_group_id == small_group_id)
        .first()
    )


def get_address_by_id(db: Session, address_id: int):
    return db.query(models.Address).get(address_id)


def get_contact_phones_by_small_group(db: Session, small_group_id: int):
    return (
        db.query(models.ContactPhone)
        .filter(models.ContactPhone.small_group_id == small_group_id)
        .all()
    )


def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_token(db: Session, token: str) -> models.User:
    return db.query(models.User).filter(models.User.hashed_password == token).first()


def create_user(db: Session, user: schemas.UserInDB) -> models.User:
    db_user = models.User(
        username=user.username,
        hashed_password=user.hashed_password,
        email=user.email,
        full_name=user.full_name,
        disabled=user.disabled,
        client_id=user.client_id,
        client_secret=user.client_secret,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_token(db: Session, token: str):
    return db.query(models.Token).filter(models.Token.token == token).first()


def create_token(db: Session, token: str, user_id: int):
    db_token = models.Token(token=token, user_id=user_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def update_user_scopes(
    db: Session, user_scopes: schemas.UserScope
) -> schemas.UserScope:
    db.query(models.UserScope).filter(
        models.UserScope.user_id == user_scopes.user_id
    ).delete()
    if user_scopes.scopes:
        for scope in user_scopes.scopes:
            db.add(
                models.UserScope(
                    user_id=user_scopes.user_id, scope=models.ScopeEnum(scope)
                )
            )
    db.commit()
    return user_scopes
