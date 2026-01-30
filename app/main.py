from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import books, members, transactions

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(members.router)
app.include_router(transactions.router)

@app.get("/")
def home():
    return {"message": "Library API running"}