from fastapi import FastAPI
from app.routes import status
from app.database import Base, engine
from app import models

app = FastAPI()

app.include_router(status.router, prefix="/status")
Base.metadata.create_all(bind=engine)