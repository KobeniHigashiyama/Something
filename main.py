from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from items_views import router as items_router
from user.views import router as users_router
from v1 import router as v1_router
from core.model import Base, db


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(v1_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
