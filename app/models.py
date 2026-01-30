from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int

class Member(BaseModel):
    name: str
    email: str
    phone: str

class Transaction(BaseModel):
    book_id: str
    member_id: str
    issue_date: datetime = datetime.utcnow()
    return_date: Optional[datetime] = None