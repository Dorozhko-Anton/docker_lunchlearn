from fastapi import FastAPI, Depends
from app.config import get_settings, Settings


app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong! MODIFIED"}


@app.get("/async_ping")
async def async_pong():
    return {"ping": "async pong!"}



@app.get("/ping2")
def pong2(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
    }

