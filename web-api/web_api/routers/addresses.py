from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from typing import Annotated

import schemas
import repository
from dependencies import get_db
from middlewares.auth import oauth2_scheme, Scope
from routers.accounts import get_current_user

router = APIRouter(
    prefix="/addresses",
    tags=["addresses"],
    dependencies=[Depends(get_db), Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{address_id}", response_model=schemas.Address)
async def read_small_groups_addresses(
    address_id: int, 
    current_user: Annotated[schemas.User, Security(get_current_user, scopes=[Scope.ADDRESS_READ])], 
    db: Session = Depends(get_db)
) -> schemas.Address:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    address = repository.get_address_by_id(db, address_id)
    if not address:
        raise HTTPException(status_code=404)
    return address
