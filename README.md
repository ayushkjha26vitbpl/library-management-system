# Library Management Console App

This is a simple **Python-based Library Management System** that I made as my first-semester project for the Course Domain evaluation.

The project runs in the command line and provides some basic features that you would expect in a small library system, such as adding books, viewing the catalog, searching for books, and keeping track of whether a book has been issued or returned.

The book data is saved locally in a JSON file, so the information is not lost when the program is closed.

## Features

- Add new books to the library
- Store book details such as:
  - Book title
  - Author
  - Accession ID
  - Shelf location
- View the complete list of books
- Search for books using the title or author name
- Issue and return books
- Check whether a book is currently available
- Save and load book data using a local JSON file
- Simple menu-based command-line interface

## Requirements

Before running the project, make sure you have:

- **Python 3.8 or above**
- A terminal or command prompt

No external Python libraries are required since the project uses Python's built-in modules.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ayushkjha26vitbpl/library-management-system.git
```

### 2. Open the project folder

```bash
cd library-management-system
```

### 3. Run the program

```bash
python main.py
```

The program will open in the terminal and show a menu from which you can choose the required operation.

## Data Storage

The program uses a JSON file called `books_data.json` to store the library data.

This means that books added during one session can still be available when the program is opened again.

## Project Purpose

The main purpose of this project was to practice the basics of Python programming and understand how different concepts can be combined to build a small working application.

Some of the concepts used in the project include:

- Classes and objects
- Functions
- Conditional statements
- Loops
- Dictionaries
- File handling
- JSON
- User input and validation

## Author

**Ayush Kumar Jha**

B.Tech CSE (Health Informatics)  
VIT Bhopal University