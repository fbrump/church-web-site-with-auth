from uuid import UUID
from typing import Any
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import repository
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API
@app.get("/small-groups/", response_model=list[schemas.SmallGroup])
async def read_small_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    small_groups = repository.get_small_groups(db, skip=skip, limit=limit)
    return small_groups

@app.post("/small-groups/", response_model=schemas.SmallGroup)
def create_small_group(small_group: schemas.SmallGroupCreate, db: Session = Depends(get_db)):
    db_small_group = repository.get_small_group_by_title(db, title=small_group.title)
    if db_small_group:
        raise HTTPException(status_code=400, detail="Small group already registered")
    return repository.create_small_group(db=db, small_group=small_group)

@app.get("/small-groups/{small_group_id}/", response_model=schemas.SmallGroup)
async def read_small_group(small_group_id: UUID, db: Session = Depends(get_db)) -> schemas.SmallGroup:
    print(small_group_id)
    small_group = repository.get_small_group(db, small_group_id)
    print(small_group)
    if not small_group:
        raise HTTPException(status_code=400, detail="Small group does not find")
    return small_group

@app.get("/small-groups/{small_group_id}/addresses/", response_model=schemas.Address)
async def read_small_groups_addresses(small_group_id: UUID, db: Session = Depends(get_db)) -> schemas.Address:
    addresses = repository.get_address_by_small_group(db, small_group_id)
    return addresses

@app.get("/small-groups/{small_group_id}/addresses/{address_id}", response_model=schemas.Address)
async def read_small_groups_addresses(small_group_id: UUID, address_id:int, db: Session = Depends(get_db)) -> schemas.Address:
    address = repository.get_address_by_id(db, small_group_id, address_id)
    if not address:
        raise HTTPException(status_code=400, detail="Address does not find")
    return address

@app.get("/small-groups/{small_group_id}/contacts/", response_model=list[schemas.ContactPhone])
async def read_small_group_contacts(small_group_id: UUID, db: Session = Depends(get_db)) -> list[schemas.ContactPhone]:
    contacts = repository.get_contact_phones_by_small_group(db, small_group_id)
    return contacts
