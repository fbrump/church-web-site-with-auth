from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
import repository
from dependencies import get_db

router = APIRouter(
    prefix="/addresses",
    tags=["addresses"],
    dependencies=[Depends(get_db)],
    responses={404: { "description": "Not found"}}
)

@router.get("/{address_id}", response_model=schemas.Address)
async def read_small_groups_addresses(address_id:int, db: Session = Depends(get_db)) -> schemas.Address:
    address = repository.get_address_by_id(db, address_id)
    if not address:
        raise HTTPException(status_code=404)
    return address