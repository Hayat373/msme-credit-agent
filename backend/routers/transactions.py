# backend/routers/transactions.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .. import models
from ..db import SessionLocal

router = APIRouter(prefix="/transactions", tags=["Transactions"])

class TransactionData(BaseModel):
    business_id: int
    amount: float
    type: str
    channel: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_transaction(data: TransactionData, db: Session = Depends(get_db)):
    transaction = models.Transaction(
        business_id=data.business_id,
        amount=data.amount,
        type=data.type,
        channel=data.channel,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return {"message": "✅ Transaction uploaded", "data": transaction.__dict__}
