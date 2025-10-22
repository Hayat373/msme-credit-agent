from fastapi import FastAPI
from .routers import onboarding, transactions, scoring
from .models import Base
from .db import engine

# Create DB tables if not exist
Base.metadata.create_all(bind=engine)

# Create the FastAPI instance
app = FastAPI(
    title="MSME Credit Agent API",
    description="Custom API for onboarding and credit scoring using your own backend.",
    version="0.1.0"
)

# Register routers
app.include_router(onboarding.router)
app.include_router(transactions.router)
app.include_router(scoring.router)


@app.get("/")
async def root():
    return {"message": "Welcome to MSME Credit Agent API 🚀"}

@app.get("/health")
async def health():
    return {"status": "ok"}
