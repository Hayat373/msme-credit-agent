# backend/routers/onboarding.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .. import models
from ..db import SessionLocal

router = APIRouter(prefix="/onboard", tags=["Onboarding"])

class BusinessData(BaseModel):
    name: str
    phone: str
    years_operating: int
    monthly_revenue: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def onboard_business(data: BusinessData, db: Session = Depends(get_db)):
    new_business = models.Business(
        name=data.name,
        phone=data.phone,
        started_at=data.years_operating,
        monthly_revenue=data.monthly_revenue,
    )
    db.add(new_business)
    db.commit()
    db.refresh(new_business)
    return {"message": "✅ Business onboarded successfully!", "data": new_business.__dict__}
