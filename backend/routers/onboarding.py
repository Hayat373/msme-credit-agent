from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/onboard", tags=["Onboarding"])

# Define input data structure
class BusinessData(BaseModel):
    name: str
    owner_name: str
    phone: str
    years_operating: int
    monthly_revenue: float

# Temporary in-memory store (later: PostgreSQL)
fake_db = []

@router.post("/")
async def onboard_business(data: BusinessData):
    """Simulate onboarding a business."""
    record = data.model_dump()
    record["business_id"] = len(fake_db) + 1
    fake_db.append(record)
    return {"message": "Business onboarded successfully!", "data": record}
