from fastapi import Depends, FastAPI
from fastapi_limiter.depends import RateLimiter
from pyrate_limiter import Duration, Limiter, Rate

app = FastAPI()

limiter = Limiter(Rate(2, Duration.SECOND * 5))


@app.get("/", dependencies=[Depends(RateLimiter(limiter=limiter))])
async def index():
    return {"msg": "Hello world!"}
