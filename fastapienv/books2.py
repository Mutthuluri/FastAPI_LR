from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)


BOOKS = [
    Book(1, "Computer Science", "Maya Bennett", "Nice book to study", 5),
    Book(2, "Mathematics", "Ethan Brooks", "Description Two", 4),
    Book(3, "Physics", "Sofia Carter", "Interesting book to study", 5),
    Book(4, "Chemistry", "Liam Foster", "Useful book to study", 4),
    Book(5, "Biology", "Nora Mitchell", "Good book to study", 5),
    Book(6, "History", "Oliver Reed", "Fascinating book to study", 2),
    Book(7, "English Literature", "Ava Sullivan", "Great book to study", 5),
    Book(8, "Data Science", "Noah Parker", "Practical book to study", 5),
    Book(9, "Artificial Intelligence", "Isla Morgan", "Modern book to study", 4)
]

@app.get("/books")
def read_all_books():
    return BOOKS
    

@app.post("/create-book")
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book

@app.put("/update-book")
def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book