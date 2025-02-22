from pydantic import BaseModel

class PaymentTransactionCreate(BaseModel):
    amount: float
    currency: str

class PaymentTransaction(PaymentTransactionCreate):
    id: int
    status: str

    class Config:
        orm_mode = True
