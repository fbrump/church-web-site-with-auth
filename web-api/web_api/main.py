from fastapi import FastAPI

import models
from database import engine
from routers import addresses, small_groups, accounts
from middlewares.cors import setup_cors


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

setup_cors(app)

app.include_router(accounts.router, prefix="/api/v1")
app.include_router(small_groups.router, prefix="/api/v1")
app.include_router(addresses.router, prefix="/api/v1")
