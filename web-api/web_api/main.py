from fastapi import FastAPI

import models
from database import engine
from routers import addresses, small_groups


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(small_groups.router, prefix="/api/v1")
app.include_router(addresses.router, prefix="/api/v1")