from sqlalchemy.orm import Session

from . import models


def get_small_group(db: Session, small_group_id: int):
    return db.query(models.SmallGroup).filter(models.SmallGroup.id == small_group_id).first()

def get_small_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SmallGroup).filter(models.SmallGroup.is_active == True).offset(skip).limit(limit).all()

def get_address_by_small_group(db: Session, small_group_id: int):
    return db.query(models.Address).filter(models.Address.small_group_id == small_group_id).first()

def get_contact_phones_by_small_group(db: Session, small_group_id: int):
    return db.query(models.ContactPhone).filter(models.ContactPhone.small_group_id == small_group_id).all()
