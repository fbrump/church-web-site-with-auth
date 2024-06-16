import enum
import uuid
from typing import List

from database import Base
from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ScopeEnum(enum.Enum):
    ACCOUNT_READ = "account:read"
    ACCOUNT_WRITE = "account:write"
    SMALL_GROUP_READ = "small-group:read"
    SMALL_GROUP_WRITE = "small-group:write"
    ADDRESS_READ = "address:read"


class SmallGroup(Base):
    __tablename__ = "small_groups"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    weekday = Column(String)
    start_at = Column(String(5))
    finish_at = Column(String(5))
    is_active = Column(Boolean, default=True)

    contact_phones: Mapped[List["ContactPhone"]] = relationship(
        back_populates="small_group"
    )
    address: Mapped["Address"] = relationship(back_populates="small_group")


class ContactPhone(Base):
    __tablename__ = "contact_phones"

    id = Column(Integer, primary_key=True)
    country_code = Column(String(4), nullable=False)
    number = Column(String(10), nullable=False)
    reference = Column(String(160), nullable=True)

    small_group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("small_groups.id"))
    small_group: Mapped["SmallGroup"] = relationship(back_populates="contact_phones")


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String(160), nullable=False)
    reference = Column(String(250), nullable=True)
    number = Column(String(5), nullable=True)
    zip_code = Column(String(9), nullable=True)
    neighborhood = Column(String(50))
    city = Column(String(160), nullable=False)
    state = Column(String(160), nullable=False)
    country = Column(String(160), nullable=False)

    small_group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("small_groups.id"))
    small_group: Mapped["SmallGroup"] = relationship(
        back_populates="address", single_parent=True
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username = Column(String(250), nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String(250), nullable=True)
    full_name = Column(String(250), nullable=True)
    client_id = Column(String, nullable=True)
    client_secret = Column(String, nullable=True)
    disabled = Column(Boolean, default=True)
    scopes: Mapped[List["UserScope"]] = relationship(back_populates="user")


class UserScope(Base):
    __tablename__ = "user_scopes"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    scope = Column(Enum(ScopeEnum), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="scopes")


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
