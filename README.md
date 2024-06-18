# Books Advanced API by Hasan

## Overview

The Books Advanced API is a simple RESTful API for managing a collection of books. The API provides endpoints for creating, reading, updating, and deleting books, as well as querying books by specific criteria such as rating and publication year.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- Uvicorn (for running the server)

## Installation

1. Clone the repository or download the code files.
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required dependencies:
    ```bash
    pip install fastapi pydantic uvicorn
    ```

## Running the API

To start the API server, run the following command:
```bash
uvicorn books:app --reload
```

## API Documentation

For a detailed interactive API documentation, visit the following Postman link: [Postman API Documentation](https://documenter.getpostman.com/view/7604536/2sA3XSC1vk)

## API Endpoints

### Get All Books
- **URL**: `/books`
- **Method**: `GET`
- **Status Code**: `200 OK`
- **Description**: Returns a list of all books.
- **Example Response**:
    ```json
    [
        {
            "id": 1,
            "title": "CS 1101",
            "author": "Hasan",
            "description": "This is Hasan's great book",
            "rating": 5.0,
            "publish": 2001
        },
        ...
    ]
    ```

### Get Book by ID
- **URL**: `/books/{book_id}`
- **Method**: `GET`
- **Status Code**: `200 OK` or `404 Not Found`
- **Description**: Returns a book with the specified ID.
- **Example Response**:
    ```json
    {
        "id": 1,
        "title": "CS 1101",
        "author": "Hasan",
        "description": "This is Hasan's great book",
        "rating": 5.0,
        "publish": 2001
    }
    ```

### Get Books by Rating
- **URL**: `/books/`
- **Method**: `GET`
- **Query Parameter**: `book_rating` (float)
- **Status Code**: `200 OK`
- **Description**: Returns a list of books with the specified rating.
- **Example Response**:
    ```json
    [
        {
            "id": 1,
            "title": "CS 1101",
            "author": "Hasan",
            "description": "This is Hasan's great book",
            "rating": 5.0,
            "publish": 2001
        },
        ...
    ]
    ```

### Get Books by Publication Year
- **URL**: `/books/publish/`
- **Method**: `GET`
- **Query Parameter**: `published` (int)
- **Status Code**: `200 OK`
- **Description**: Returns a list of books published in the specified year.
- **Example Response**:
    ```json
    [
        {
            "id": 1,
            "title": "CS 1101",
            "author": "Hasan",
            "description": "This is Hasan's great book",
            "rating": 5.0,
            "publish": 2001
        },
        ...
    ]
    ```

### Create a New Book
- **URL**: `/create-book`
- **Method**: `POST`
- **Status Code**: `201 Created`
- **Description**: Creates a new book with the provided details.
- **Request Body**:
    ```json
    {
        "title": "New Book",
        "author": "Author Name",
        "description": "This is a description of the new book.",
        "rating": 4.5,
        "publish": 2020
    }
    ```
- **Example Response**:
    ```json
    {
        "message": "Book created successfully",
        "book": {
            "id": 8,
            "title": "New Book",
            "author": "Author Name",
            "description": "This is a description of the new book.",
            "rating": 4.5,
            "publish": 2020
        }
    }
    ```

### Update an Existing Book
- **URL**: `/books/update_book`
- **Method**: `PUT`
- **Status Code**: `204 No Content` or `404 Not Found`
- **Description**: Updates the details of an existing book.
- **Request Body**:
    ```json
    {
        "id": 1,
        "title": "Updated Title",
        "author": "Updated Author",
        "description": "Updated description.",
        "rating": 4.8,
        "publish": 2021
    }
    ```

### Delete a Book
- **URL**: `/books/{book_id}`
- **Method**: `DELETE`
- **Status Code**: `204 No Content` or `404 Not Found`
- **Description**: Deletes a book with the specified ID.

## Models

### Book
```python
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
```

### BookRequest (Pydantic Model)
```python
class BookRequest(BaseModel):
    id: Optional[int] = Field(None, description="ID is not required. It will be auto-generated")
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
```

## Helper Functions

### Find Book ID
```python
def find_book_id(book: Book):
    book.id = 0 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
```

## Error Handling

- **404 Not Found**: Raised when a book with the specified ID is not found.
- **Query Parameter Validation**: Ensures the rating and publication year fall within the valid ranges.

## Example

To test the API, you can use tools like `curl`, Postman, or the FastAPI interactive docs available at `http://127.0.0.1:8000/docs` after running the server.

```bash
# Example to get all books
curl -X GET "http://127.0.0.1:8000/books" -H "accept: application/json"
```
