from fastapi import FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, book_id, title, author, description, rating):
        self.id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'CS 1101', 'Hasan', 'This is hasan great book', '4'),
    Book(2, 'CS 1102', 'Hasan', 'This is hasan 2 great book', '4'),
    Book(3, 'CS 1103', 'Hasan', 'This is hasan 3 great book', '4'),
    Book(4, 'CS 1104', 'Hasan', 'This is hasan 4 great book', '4'),
    Book(5, 'CS 1105', 'Hasan', 'This is hasan 5 great book', '4'),
    Book(6, 'CS 1106', 'Hasan', 'This is hasan 6 great book', '4'),
    Book(7, 'CS 1107', 'Hasan', 'This is hasan 6 great book', '4'),
]




@app.get("/books")
async def read_all_books():
    return BOOKS