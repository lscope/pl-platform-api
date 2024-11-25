from contextlib import asynccontextmanager
from fastapi import FastAPI

from .database import populate_db




@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Create db tables before the app startup
        populate_db()

        yield # Yield control to the FastAPI app. When the app is shutdown, the code after yield is executed
    except Exception as e:
        print(e)

app: FastAPI = FastAPI(
    lifespan=lifespan,
)