# Simple Library Management System

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.students = []


    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully")

    def register_student(self, student):
        self.students.append(student)
        print("Student Registered Successfully")


    def borrow_book(self, student_id, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book Borrowed Successfully")
                else:
                    print("Book is not available")
                return
        print("Book not found")

  
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book Returned Successfully")
                return
        print("Book not found")


    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            if book.available:
                status = "Available"
            else:
                status = "Borrowed"

            print(book.book_id, "-", book.title, "-", status)




library = Library()

# Add Books
library.add_book(Book(1, "Python"))
library.add_book(Book(2, "Data Structures"))
library.add_book(Book(3, "Database Management"))

# Register Students
library.register_student(Student(101, "Vedant"))
library.register_student(Student(102, "Rahul"))

# Display Books
library.display_books()

# Borrow Book
library.borrow_book(101, 1)

# Display Books
library.display_books()

# Return Book
library.return_book(1)

# Display Books
library.display_books()
