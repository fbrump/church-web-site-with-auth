from typing import Annotated
from uuid import UUID

import repository
import schemas
from dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, Security
from middlewares.auth import Scope, get_current_user, oauth2_scheme
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/small-groups",
    tags=["small-groups"],
    dependencies=[Depends(get_db), Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


# API
@router.get("/", response_model=list[schemas.SmallGroup])
async def read_small_groups(
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.SMALL_GROUP_READ])
    ],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    small_groups = repository.get_small_groups(db, skip=skip, limit=limit)
    return small_groups


@router.post("/", response_model=schemas.SmallGroup)
def create_small_group(
    small_group: schemas.SmallGroupCreate,
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.SMALL_GROUP_WRITE])
    ],
    db: Session = Depends(get_db),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    db_small_group = repository.get_small_group_by_title(db, title=small_group.title)
    if db_small_group:
        raise HTTPException(status_code=400)
    return repository.create_small_group(db=db, small_group=small_group)


@router.get("/{small_group_id}", response_model=schemas.SmallGroup)
async def read_small_group(
    small_group_id: UUID,
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.SMALL_GROUP_READ])
    ],
    db: Session = Depends(get_db),
) -> schemas.SmallGroup:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    small_group = repository.get_small_group(db, small_group_id)
    if not small_group:
        raise HTTPException(status_code=400)
    return small_group


@router.get("/{small_group_id}/addresses/", response_model=schemas.Address)
async def read_small_groups_addresses(
    small_group_id: UUID,
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.SMALL_GROUP_READ])
    ],
    db: Session = Depends(get_db),
) -> schemas.Address:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    addresses = repository.get_address_by_small_group(db, small_group_id)
    return addresses


@router.get(
    "/{small_group_id}/contacts/",
    response_model=list[schemas.ContactPhone],
)
async def read_small_group_contacts(
    small_group_id: UUID,
    current_user: Annotated[
        schemas.User, Security(get_current_user, scopes=[Scope.SMALL_GROUP_READ])
    ],
    db: Session = Depends(get_db),
) -> list[schemas.ContactPhone]:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    contacts = repository.get_contact_phones_by_small_group(db, small_group_id)
    return contacts
