from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "Title One", "author": "Author One","category":"science", "rating": 5}, 
    {"id": 2, "title": "Title Two", "author": "Author Two", "category":"science", "rating": 4},
    {"id": 3, "title": "Title Three", "author": "Author one", "category":"history", "rating": 3},
    {"id": 4, "title": "Title Four", "author": "Author Four","category":"math", "rating": 4},
    {"id": 5, "title": "Title Five", "author": "Author one","category":"math", "rating": 5},
    {"id": 6, "title": "Title Six", "author": "Author Six","category":"math", "rating": 4}
]

@app.get("/books")
def Read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

@app.get("/books/{book_title}")
def read_book(book_title :str):
    for book in BOOKS:
        if book.get("title").lower() == book_title.lower():
            return book
    return {"message": "Book not found"}

@app.get("/books/")
def read_book_by_category(category: str):
    books_by_category = []
    for book in BOOKS:
        if book.get("category").lower() == category.lower():
            books_by_category.append(book)
    return books_by_category

@app.get("/books/rating/{book_rating}")
def read_book_by_rating(book_rating: int):
    booksofRating = []
    for book in BOOKS:
        if book.get("rating") == book_rating:
            booksofRating.append(book)
    return booksofRating


@app.get("/books/author/{book_author}")
def read_category_book_by_author(book_author: str, category: str):
    books_by_author_and_category = []
    for book in BOOKS:
        if book.get("author").lower() == book_author.lower() and book.get("category").lower() == category.lower():
            books_by_author_and_category.append(book)
    return books_by_author_and_category

@app.post("/books")
def create_book(new_book: dict):
    BOOKS.append(new_book)



@app.put("/books/updatebook")
def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").lower() == updated_book.get("title").lower():
            BOOKS[i] = updated_book

@app.delete("/books/deletebook/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").lower() == book_title.lower():
            BOOKS.pop(i)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}


# Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

@app.get("/books/specific_author/{book_author}")
def get_books_by_author(book_author: str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").lower() == book_author.lower():
            books_by_author.append(book)
    return books_by_author