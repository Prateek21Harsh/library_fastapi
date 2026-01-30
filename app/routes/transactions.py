from fastapi import APIRouter
from app.database import transactions_collection

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/issue")
def issue_book(data: dict):
    result = transactions_collection.insert_one(data)
    return {"id": str(result.inserted_id)}

@router.post("/return/{transaction_id}")
def return_book(transaction_id: str):
    transactions_collection.update_one(
        {"_id": transaction_id},
        {"$set": {"return_date": None}}
    )
    return {"message": "Book returned"}