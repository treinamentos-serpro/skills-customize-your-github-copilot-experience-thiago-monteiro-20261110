from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookCreate(BaseModel):
    title: str
    author: str


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate) -> Book:
    raise NotImplementedError


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int) -> Book:
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
