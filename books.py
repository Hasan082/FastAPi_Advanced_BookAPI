from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status


app = FastAPI(title="Books Advanced API by Hasan", version='1.0.0')


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    publish: int

    def __init__(self, id, title, author, description, rating, publish):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish = publish


class BookRequest(BaseModel):
    id: Optional[int] = Field(None, description="Id is not required. It will auto generated")
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=500)
    rating: float = Field(ge=0, le=5)
    publish: int = Field(ge=1999, le=2024)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    'title': 'Book Title',
                    'author': 'Author Name',
                    'description': 'This is an example of a book description.',
                    'rating': 4.5,
                    'publish': 1999,
                }
            ]
        }


BOOKS = [
    Book(1, 'CS 1101', 'Hasan', 'This is hasan 1 great book', 5.00, publish=2001),
    Book(2, 'CS 1102', 'Hasan', 'This is hasan 2 great book', 4.75, publish=1999),
    Book(3, 'CS 1103', 'Hasan', 'This is hasan 3 great book', 4.25, publish=2009),
    Book(4, 'CS 1104', 'Hasan', 'This is hasan 4 great book', 5.00, publish=2003),
    Book(5, 'CS 1105', 'Hasan', 'This is hasan 5 great book', 4.00, publish=2007),
    Book(6, 'CS 1106', 'Hasan', 'This is hasan 6 great book', 4.00, publish=2009),
    Book(7, 'CS 1107', 'Hasan', 'This is hasan 6 great book', 4.00, publish=2009),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: float = Query(gt=-1, lt=5.01)):
    return_all_books_with_rating = []
    for book in BOOKS:
        if book.rating == book_rating:
            return_all_books_with_rating.append(book)
    return return_all_books_with_rating


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_publish(published: int = Query(ge=1999, le=2014)):
    books_to_returns = []
    for book in BOOKS:
        if book.publish == published:
            books_to_returns.append(book)
    return books_to_returns


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    new_book_id = find_book_id(new_book)
    BOOKS.append(new_book_id)
    return {"message": "Book created successfully", "book": new_book}


def find_book_id(book: Book):
    book.id = 0 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = book
            book_updated = True
    if not book_updated:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Book not found")
