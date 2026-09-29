# CSE First Semester Project - Library Portal
# Built using basic Python data structures and JSON storage

import json
import os

# File where book data gets saved locally
DATA_FILE = "books_data.json"


def load_all_books():
    """Reads saved books from the JSON file if it exists."""
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # If file is corrupted or empty, start fresh
        return {}


def save_all_books(catalog):
    """Saves the current catalog dictionary back to JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(catalog, f, indent=2)


def add_new_book(catalog):
    print("\n--- ADD A NEW BOOK ---")
    book_num = input("Enter Book Accession ID: ").strip()
    
    if book_num in catalog:
        print("ERROR: A book with this ID already exists!")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    rack_no = input("Enter Shelf/Rack Number (e.g. A-12): ").strip()

    if title == "" or author == "":
        print("ERROR: Title and Author cannot be empty.")
        return

    # Store as a simple dictionary entry
    catalog[book_num] = {
        "title": title,
        "author": author,
        "shelf": rack_no if rack_no else "Unassigned",
        "issued": False
    }

    save_all_books(catalog)
    print(f"Success! Added '{title}' to the library catalog.")


def show_books(catalog):
    print("\n--- CURRENT LIBRARY CATALOG ---")
    if not catalog:
        print("No books registered in the system yet.")
        return

    for b_id, info in catalog.items():
        if info["issued"]:
            status_str = "ISSUED"
        else:
            status_str = "AVAILABLE"
            
        print(f"[{b_id}] {info['title']} by {info['author']} | Shelf: {info['shelf']} | Status: {status_str}")


def search_books(catalog):
    print("\n--- SEARCH BOOKS ---")
    query = input("Enter Title or Author keyword: ").strip().lower()
    
    if not query:
        print("Search query cannot be blank.")
        return

    found_count = 0
    for b_id, info in catalog.items():
        if query in info['title'].lower() or query in info['author'].lower():
            status = "Issued" if info["issued"] else "Available"
            print(f"-> ID: {b_id} | {info['title']} by {info['author']} ({status})")
            found_count += 1
            
    if found_count == 0:
        print("No matching books found.")


def issue_book(catalog):
    print("\n--- ISSUE BOOK ---")
    b_id = input("Enter Book ID to issue: ").strip()

    if b_id not in catalog:
        print("Book ID not found in system.")
        return

    if catalog[b_id]["issued"]:
        print("Sorry, this book is already issued to someone else.")
        return

    catalog[b_id]["issued"] = True
    save_all_books(catalog)
    print(f"Book '{catalog[b_id]['title']}' has been issued successfully!")


def return_book(catalog):
    print("\n--- RETURN BOOK ---")
    b_id = input("Enter Book ID to return: ").strip()

    if b_id not in catalog:
        print("Book ID not found in system.")
        return

    if not catalog[b_id]["issued"]:
        print("This book was not marked as issued.")
        return

    catalog[b_id]["issued"] = False
    save_all_books(catalog)
    print(f"Book '{catalog[b_id]['title']}' returned successfully!")


def main():
    books_catalog = load_all_books()
    
    while True:
        print("\n=================================")
        print("    VIT LIBRARY MANAGEMENT CLI   ")
        print("=================================")
        print("1. View All Books")
        print("2. Add New Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        
        user_choice = input("\nSelect an option (1-6): ").strip()

        if user_choice == "1":
            show_books(books_catalog)
        elif user_choice == "2":
            add_new_book(books_catalog)
        elif user_choice == "3":
            search_books(books_catalog)
        elif user_choice == "4":
            issue_book(books_catalog)
        elif user_choice == "5":
            return_book(books_catalog)
        elif user_choice == "6":
            print("\nClosing Library System. Have a nice day!")
            break
        else:
            print("Invalid choice, please select between 1 and 6.")


if __name__ == "__main__":
    main()