from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.database.connection import (
    close_connection,
    verify_connection,
)

from app.routes.requirements import router as requirements_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting TestGraph API...")

    try:
        if verify_connection():
            print("Connected to CognoDB")
    except Exception as exc:
        print(f"Could not connect to CognoDB: {exc}")

    yield

    close_connection()
    print("Database connection closed")


app = FastAPI(
    title="TestGraph",
    description="Testing Traceability and Impact Analysis",
    version="1.0.0",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://test-graph-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(requirements_router)

@app.get("/")
def root():
    return {
        "message": "TestGraph API is running"
    }


@app.get("/health")
def health():
    try:
        connected = verify_connection()

        return {
            "status": "healthy" if connected else "unhealthy",
            "database": "connected" if connected else "not connected",
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "connection failed",
        }