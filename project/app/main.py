from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
import redis

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


@app.get("/redis")
def redis_check():
    r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
    r.set('foo', 'bar')
    return {
        'redis_foo' : r.get('foo'),
        'OK' : r.get('foo') == "bar"
    }

