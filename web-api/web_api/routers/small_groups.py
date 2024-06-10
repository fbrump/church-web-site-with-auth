from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

import schemas
import repository
from dependencies import get_db

router = APIRouter(
    prefix="/small-groups",
    tags=["small-groups"],
    dependencies=[Depends(get_db)],
    responses={404: { "description": "Not found"}}
)

# API
@router.get("/small-groups/", response_model=list[schemas.SmallGroup])
async def read_small_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    small_groups = repository.get_small_groups(db, skip=skip, limit=limit)
    return small_groups

@router.post("/small-groups/", response_model=schemas.SmallGroup)
def create_small_group(small_group: schemas.SmallGroupCreate, db: Session = Depends(get_db)):
    db_small_group = repository.get_small_group_by_title(db, title=small_group.title)
    if db_small_group:
        raise HTTPException(status_code=400)
    return repository.create_small_group(db=db, small_group=small_group)

@router.get("/small-groups/{small_group_id}/", response_model=schemas.SmallGroup)
async def read_small_group(small_group_id: UUID, db: Session = Depends(get_db)) -> schemas.SmallGroup:
    print(small_group_id)
    small_group = repository.get_small_group(db, small_group_id)
    print(small_group)
    if not small_group:
        raise HTTPException(status_code=400)
    return small_group

@router.get("/small-groups/{small_group_id}/addresses/", response_model=schemas.Address)
async def read_small_groups_addresses(small_group_id: UUID, db: Session = Depends(get_db)) -> schemas.Address:
    addresses = repository.get_address_by_small_group(db, small_group_id)
    return addresses

@router.get("/small-groups/{small_group_id}/contacts/", response_model=list[schemas.ContactPhone])
async def read_small_group_contacts(small_group_id: UUID, db: Session = Depends(get_db)) -> list[schemas.ContactPhone]:
    contacts = repository.get_contact_phones_by_small_group(db, small_group_id)
    return contacts