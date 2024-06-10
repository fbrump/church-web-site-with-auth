from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Time, Uuid
from sqlalchemy.orm import relationship

from .database import Base


class SmallGroup(Base):
    __tablename__ = "small_groups"

    id = Column(Uuid, primary_key=True)
    title = Column(String, unique=True, index=True)
    weekday = Column(String)
    start_at = Column(Time)
    finish_at = Column(Time)
    is_active = Column(Boolean, default=True)
    
    contact_phones = relationship("ContactPhone", back_populates="small_group")
    address = relationship("Address", back_populates="small_group")

class ContactPhone(Base):
    __tablename__ = "contact_phones"
    
    id = Column(Integer, primary_key=True)
    country_code = Column(String(4), nullable=False)
    number = Column(String(10), nullable=False)
    reference = Column(String(160), nullable=True)
    
    small_group_id = Column(Uuid, ForeignKey("small_groups.id"))
    small_group = relationship("SmallGroup", back_populates="contact_phones")

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
    
    small_group_id = Column(Uuid, ForeignKey("small_groups.id"))
    small_group = relationship("SmallGroup", back_populates="address", single_parent=True)
  