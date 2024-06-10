from uuid import UUID
from sqlalchemy.orm import Session

import models, schemas


def get_small_group(db: Session, small_group_id: UUID):
    return db.query(models.SmallGroup).get(small_group_id)

def get_small_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SmallGroup).filter(models.SmallGroup.is_active == True).offset(skip).limit(limit).all()

def create_small_group(db: Session, small_group: schemas.SmallGroupCreate):
    db_small_group = models.SmallGroup(
        title=small_group.title,
        weekday=small_group.weekday,
        start_at=small_group.start_at,
        finish_at=small_group.finish_at
    )
    db.add(db_small_group)
    db_address=models.Address(
            street=small_group.address.street,
            reference=small_group.address.reference,
            number=small_group.address.number,
            zip_code=small_group.address.zip_code,
            neighborhood=small_group.address.neighborhood,
            city=small_group.address.city,
            state=small_group.address.state,
            country=small_group.address.country,
            small_group = db_small_group
        )
    db.add(db_address)
    db.commit()
    db.refresh(db_small_group)
    return db_small_group

def get_small_group_by_title(db: Session, title: str):
    return db.query(models.SmallGroup).filter(models.SmallGroup.title == title).first()

def get_address_by_small_group(db: Session, small_group_id: UUID):
    return db.query(models.Address).filter(models.Address.small_group_id == small_group_id).first()

def get_address_by_id(db: Session, small_group_id: UUID, address_id:int):
    address = db.query(models.Address).get(address_id)
    if address and not address.small_group_id == small_group_id:
        print(f"Small Group ID is different")
        print(f"Database: {address.small_group_id}")
        print(f"Filter: {small_group_id}")
        return None
    return address

def get_contact_phones_by_small_group(db: Session, small_group_id: int):
    return db.query(models.ContactPhone).filter(models.ContactPhone.small_group_id == small_group_id).all()
