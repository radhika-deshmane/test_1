# Library Management System
# This project demonstrates file handling,
# object-oriented programming, loops,
# conditionals, and data management.

import json
import os
from datetime import datetime

DATA_FILE = "library_data.json"


# -----------------------------
# Book Class
# -----------------------------
class Book:

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "quantity": self.quantity
        }


# -----------------------------
# Library Class
# -----------------------------
class Library:

    def __init__(self):
        self.books = []
        self.load_data()

    # Load data from JSON file
    def load_data(self):

        if os.path.exists(DATA_FILE):

            with open(DATA_FILE, "r") as file:
                data = json.load(file)

                for item in data:
                    book = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["quantity"]
                    )

                    self.books.append(book)

    # Save data to JSON file
    def save_data(self):

        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # Add new book
    def add_book(self):

        print("\n--- Add New Book ---")

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        quantity = int(input("Enter Quantity: "))

        for book in self.books:

            if book.book_id == book_id:
                print("Book ID already exists.\n")
                return

        new_book = Book(book_id, title, author, quantity)

        self.books.append(new_book)

        self.save_data()

        print("Book added successfully.\n")

    # View all books
    def view_books(self):

        print("\n--- Available Books ---")

        if len(self.books) == 0:
            print("No books available.\n")
            return

        for book in self.books:

            print(f"""
Book ID   : {book.book_id}
Title     : {book.title}
Author    : {book.author}
Quantity  : {book.quantity}
------------------------------------
""")

    # Search book by title
    def search_book(self):

        keyword = input("Enter title keyword: ").lower()

        found = False

        for book in self.books:

            if keyword in book.title.lower():

                print(f"""
Book Found
--------------------------
Book ID   : {book.book_id}
Title     : {book.title}
Author    : {book.author}
Quantity  : {book.quantity}
""")

                found = True

        if not found:
            print("No matching books found.\n")

    # Update book details
    def update_book(self):

        book_id = input("Enter Book ID to update: ")

        for book in self.books:

            if book.book_id == book_id:

                print("\nEnter New Details")

                book.title = input("New Title: ")
                book.author = input("New Author: ")
                book.quantity = int(input("New Quantity: "))

                self.save_data()

                print("Book updated successfully.\n")

                return

        print("Book not found.\n")

    # Delete book
    def delete_book(self):

        book_id = input("Enter Book ID to delete: ")

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                self.save_data()

                print("Book deleted successfully.\n")

                return

        print("Book not found.\n")

    # Borrow book
    def borrow_book(self):

        book_id = input("Enter Book ID to borrow: ")

        for book in self.books:

            if book.book_id == book_id:

                if book.quantity > 0:

                    book.quantity -= 1

                    self.save_data()

                    print("Book borrowed successfully.")
                    print("Borrow Date:", datetime.now())

                    return

                else:
                    print("Book out of stock.\n")
                    return

        print("Book not found.\n")

    # Return book
    def return_book(self):

        book_id = input("Enter Book ID to return: ")

        for book in self.books:

            if book.book_id == book_id:

                book.quantity += 1

                self.save_data()

                print("Book returned successfully.")
                print("Return Date:", datetime.now())

                return

        print("Book not found.\n")

    # Display menu
    def menu(self):

        while True:

            print("""
====================================
      LIBRARY MANAGEMENT SYSTEM
====================================
1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Delete Book
6. Borrow Book
7. Return Book
8. Exit
====================================
""")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.update_book()

            elif choice == "5":
                self.delete_book()

            elif choice == "6":
                self.borrow_book()

            elif choice == "7":
                self.return_book()

            elif choice == "8":
                print("Thank you for using Library System.")
                break

            else:
                print("Invalid choice. Please try again.\n")


# -----------------------------
# Main Program
# -----------------------------
def main():

    library = Library()

    library.menu()


if __name__ == "__main__":
    main()