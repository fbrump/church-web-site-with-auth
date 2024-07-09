from typing import Union
from uuid import UUID

import models
from pydantic import BaseModel


class ContactPhoneBase(BaseModel):
    contry_code: str
    number: str
    reference: str | None = None


class ContactPhone(ContactPhoneBase):
    id: UUID
    small_group_id: UUID

    class Config:
        from_attributes = True


class AddressBase(BaseModel):
    street: str
    reference: str | None = None
    number: str | None = None
    zip_code: str | None = None
    neighborhood: str
    city: str
    state: str
    country: str


class AddressCreate(AddressBase): ...


class Address(AddressBase):
    id: int
    small_group_id: UUID

    class Config:
        from_attributes = True


class SmallGroupBase(BaseModel):
    title: str
    weekday: str | None = None
    start_at: str | None = None
    finish_at: str | None = None


class SmallGroupCreate(SmallGroupBase):
    address: AddressCreate


class SmallGroup(SmallGroupBase):
    id: UUID
    is_active: bool
    contact_phones: list[ContactPhone] = []
    address: Address

    class Config:
        from_attributes = True


class UserScopeBase(BaseModel):
    scopes: list[str] = []


class UserScope(UserScopeBase):
    user_id: UUID


class UserScopeUpdate(UserScopeBase): ...


class UserBase(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = False
    client_id: Union[str, None] = None
    client_secret: Union[str, None] = None
    scopes: list[str] = []

class User(UserBase):
    def mapper(model: models.User):
        return User(
            username=model.username,
            email=model.email,
            full_name=model.full_name,
            disabled=model.disabled,
            client_id=model.client_id,
            client_secret=model.client_secret,
            scopes=[item.scope for item in model.scopes] if model.scopes else None,
        )


class UserInDB(User):
    hashed_password: str
    client_secret: Union[str, None] = None


class UserCreate(UserBase):
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []
