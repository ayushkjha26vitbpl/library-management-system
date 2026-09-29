```python
import json
import os


class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def get_data(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }


class Library:
    def __init__(self):
        self.file_name = "library_data.json"
        self.books = {}
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

            for book_id, book in data.items():
                self.books[book_id] = Book(
                    book["book_id"],
                    book["title"],
                    book["author"],
                    book["issued"]
                )

        except (json.JSONDecodeError, FileNotFoundError):
            self.books = {}

    def save_books(self):
        data = {}

        for book_id, book in self.books.items():
            data[book_id] = book.get_data()

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        if not book_id or not title or not author:
            print("Please enter all the details.")
            return

        if book_id in self.books:
            print("A book with this ID already exists.")
            return

        self.books[book_id] = Book(book_id, title, author)
        self.save_books()

        print("Book added successfully.")

    def show_books(self):
        if not self.books:
            print("There are no books in the library.")
            return

        print("\n----- Library Books -----")

        for book in self.books.values():
            if book.issued:
                status = "Issued"
            else:
                status = "Available"

            print(
                f"ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Author: {book.author} | "
                f"Status: {status}"
            )

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        if self.books[book_id].issued:
            print("This book has already been issued.")
            return

        self.books[book_id].issued = True
        self.save_books()

        print("Book issued successfully.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        if not self.books[book_id].issued:
            print("This book is already available.")
            return

        self.books[book_id].issued = False
        self.save_books()

        print("Book returned successfully.")


def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```