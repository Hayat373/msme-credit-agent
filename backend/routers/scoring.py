# backend/routers/scoring.py
from fastapi import APIRouter

router = APIRouter(prefix="/score", tags=["Scoring"])

@router.get("/{business_id}")
def score_request(business_id: int):
    # Later: calculate credit score using ML
    return {"business_id": business_id, "score": 72.5, "advice": "Increase monthly revenue consistency"}
