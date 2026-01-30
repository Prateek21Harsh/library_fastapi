from fastapi import APIRouter
from app.database import books_collection
from app.models import Book

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/")
def add_book(book: Book):
    result = books_collection.insert_one(book.model_dump())
    return {"id": str(result.inserted_id)}

@router.get("/")
def get_books():
    books = []
    for book in books_collection.find():
        book["_id"] = str(book["_id"])
        books.append(book)
    return books