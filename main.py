import json
import os

class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

    @staticmethod
    def from_dict(data):
        return Book(data["book_id"], data["title"], data["author"], data["is_issued"])


class Library:
    def __init__(self, data_file="library_data.json"):
        self.data_file = data_file
        self.books = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    data = json.load(f)
                    for b_id, b_info in data.items():
                        self.books[b_id] = Book.from_dict(b_info)
                except json.JSONDecodeError:
                    self.books = {}

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump({b_id: book.to_dict() for b_id, book in self.books.items()}, f, indent=4)

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"\n[!] Book ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        self.save_data()
        print(f"\n[+] Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("\n[-] No books found in the library.")
            return
        print("\n--- Library Catalog ---")
        for book in self.books.values():
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

    def issue_book(self, book_id):
        if book_id not in self.books:
            print(f"\n[!] Book ID {book_id} not found.")
            return
        if self.books[book_id].is_issued:
            print(f"\n[!] Book ID {book_id} is already issued.")
            return
        self.books[book_id].is_issued = True
        self.save_data()
        print(f"\n[+] Book ID {book_id} successfully issued.")

    def return_book(self, book_id):
        if book_id not in self.books:
            print(f"\n[!] Book ID {book_id} not found.")
            return
        if not self.books[book_id].is_issued:
            print(f"\n[!] Book ID {book_id} was not issued.")
            return
        self.books[book_id].is_issued = False
        self.save_data()
        print(f"\n[+] Book ID {book_id} successfully returned.")


def main():
    library = Library()
    while True:
        print("\n=============================")
        print("  LIBRARY MANAGEMENT SYSTEM  ")
        print("=============================")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            if b_id and title and author:
                library.add_book(b_id, title, author)
            else:
                print("\n[!] Inputs cannot be empty.")
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            b_id = input("Enter Book ID to issue: ").strip()
            library.issue_book(b_id)
        elif choice == "4":
            b_id = input("Enter Book ID to return: ").strip()
            library.return_book(b_id)
        elif choice == "5":
            print("\nExiting System. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()