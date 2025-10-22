# backend/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .db import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    started_at = Column(Integer, nullable=True)  # years operating
    monthly_revenue = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    ts = Column(DateTime(timezone=True), server_default=func.now())
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # e.g. "income", "expense"
    channel = Column(String, nullable=True)  # e.g. "Telebirr", "Chapa"
