import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("books.db")


def initialize_database() -> None:
    """Create the books table when it does not exist yet."""
    raise NotImplementedError


def add_book(title: str, author: str) -> None:
    """Save one book in the database."""
    raise NotImplementedError


def list_books() -> list[tuple[int, str, str]]:
    """Return all books ordered by their identifier."""
    raise NotImplementedError


def delete_book(book_id: int) -> bool:
    """Delete a book and return whether a row was removed."""
    raise NotImplementedError


def main() -> None:
    initialize_database()

    while True:
        print("\nBook Catalog")
        print("1. Add a book")
        print("2. List books")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            add_book(title, author)
            print("Book added.")
        elif choice == "2":
            books = list_books()
            if not books:
                print("No books found.")
            for book_id, title, author in books:
                print(f"{book_id}: {title} by {author}")
        elif choice == "3":
            book_id = int(input("Book ID: "))
            if delete_book(book_id):
                print("Book deleted.")
            else:
                print("No book found with that ID.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
