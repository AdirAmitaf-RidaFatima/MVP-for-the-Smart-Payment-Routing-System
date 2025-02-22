from fastapi import FastAPI
from app.routes import router
from app.database import database

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Payment API!"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router, prefix="/api")
