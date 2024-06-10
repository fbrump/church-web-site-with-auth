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
    country_code = Column(String)
    number = Column(String)
    reference = Column(String)
    
    small_group_id = Column(Uuid, ForeignKey("small_groups.id"))
    small_group = relationship("SmallGroup", back_populates="contact_phones")

class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True)
    country_code = Column(String)
    number = Column(String)

    street = Column(String(160))
    reference = Column(String(250))
    number = Column(String(5)) # models.CharField(max_length=5, null=True, blank=True)
    zip_code = Column(String(9)) # models.CharField(max_length=9, null=True, blank=True)
    neighborhood = Column(String(50)) # models.CharField(max_length=50)
    city = Column(String(160)) # models.CharField(max_length=160)
    state = Column(String(160)) # models.CharField(max_length=160)
    country = Column(String(160)) # models.CharField(max_length=160)
    
    small_group_id = Column(Uuid, ForeignKey("small_groups.id"))
    small_group = relationship("SmallGroup", back_populates="address", single_parent=True)
  