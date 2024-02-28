import uvicorn
from fastapi import FastAPI

from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Book as SchemaBook
from schema import Author as SchemaAuthor

from schema import Book
from schema import Author

from models import Book as ModelBook
from models import Author as ModelAuthor

import os
from dotenv import load_dotenv

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['postgresql://root:Password123890@localhost:5432/pizzadb'])

@app.get("/")
async def index():
    return {
        "message": "hello world"
    }

@app.post('/book/', response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id = book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.get("/book/")
async def read_book():
    book = db.session.query(ModelBook).all()
    return book
