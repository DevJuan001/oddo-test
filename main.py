from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware

from core.odoo_client import init_odoo_client
from core.redis import close_redis, init_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_odoo_client()
    redis = await init_redis(app)
    await FastAPILimiter.init(redis)
    yield
    await close_redis()

app = FastAPI(
    title="API Fastapi + Odoo",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
