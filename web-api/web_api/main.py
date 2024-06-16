import models
from database import engine
from fastapi import FastAPI
from middlewares.cors import setup_cors
from routers import accounts, addresses, small_groups

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

setup_cors(app)

app.include_router(accounts.router, prefix="/api/v1")
app.include_router(small_groups.router, prefix="/api/v1")
app.include_router(addresses.router, prefix="/api/v1")
