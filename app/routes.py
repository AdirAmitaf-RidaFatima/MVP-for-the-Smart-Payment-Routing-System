from fastapi import APIRouter, HTTPException
from app.database import database
from app.models import PaymentTransaction
from app.schemas import PaymentTransactionCreate, PaymentTransaction as PaymentTransactionResponse
from sqlalchemy import select

router = APIRouter()

@router.post("/transactions/", response_model=PaymentTransactionResponse)
async def create_transaction(transaction: PaymentTransactionCreate):
    query = PaymentTransaction.__table__.insert().values(
        amount=transaction.amount,
        currency=transaction.currency,
    )
    last_record_id = await database.execute(query)
    return {**transaction.dict(), "id": last_record_id, "status": "pending"}

@router.get("/transactions/{transaction_id}", response_model=PaymentTransactionResponse)
async def read_transaction(transaction_id: int):
    query = select(PaymentTransaction).where(PaymentTransaction.id == transaction_id)
    transaction = await database.fetch_one(query)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/", response_model=list[PaymentTransactionResponse])
async def list_transactions():
    query = select(PaymentTransaction)
    transactions = await database.fetch_all(query)
    return transactions
