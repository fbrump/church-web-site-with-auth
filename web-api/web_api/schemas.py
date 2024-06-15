from uuid import UUID
from pydantic import BaseModel
from typing import Union


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


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = False


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []
