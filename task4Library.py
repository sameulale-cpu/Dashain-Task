# Develop a simple library management program using Python functions and OOP.

# Requirements:

# - Create a "Book" class with attributes such as book ID, title, author, and availability status.
# - Create methods to display book details, borrow a book, and return a book.
# - Allow users to display all books and search for a book by ID or title.
# - Display appropriate messages when a book is unavailable or cannot be found.

class Book:
    def __init__(self, bookID, title, author, availabilitystatus):
        self.book_ID = bookID
        self.title = title
        self.author = author
        self.availability_status = availabilitystatus

    def display(self):
        print(f"""Book Id: {self.book_ID}
Title: {self.title}
author: {self.author}
Availability status: {self.availability_status}""")

    def borrow_book(self):
        if self.availability_status == True:
            self.availability_status == False
            print("You have successfully borrowed:", self.title)
        else:
            print("Sorry, Not available.")

    def returnbook(self):
        if self.availability_status == False:
            self.availability_status = True
            print("You have successfully returned:", self.title)
        else:
            print("This book is not borrowed.")


books = [
    Book(1, "Python", "John", True),
    Book(2, "Jungle Book", "Hari", True),
    Book(3, "Java", "Ram", False)
]


def displayall_books():
    for i in books:
        i.display()


def search_book():
    choice = input("Enter your choice Book's Id or title:").lower()
    found = False

    if choice == "id":
        bookid = input("Enter book id:")

        for i in books:
            if str(i.book_ID) == bookid:
                i.display()
                found = True
                break

    elif choice == "title":
        booktitle = input("Enter book title:")

        for i in books:
            if i.title == booktitle:
                i.display()
                found = True
                break
    else:
        print("Invalid search option.")

    if not found:
        print("Book not found")


def borrow_book():  # searches for the book
    search_id = input("Enter book ID:")

    for i in books:
        if str(i.book_ID) == search_id:
            i.borrow_book()  # changes the availability status
            return

    print("Book not found.")


def return_book():
    search_id = input("Enter Id of a Book to return:")

    for i in books:
        if str(i.book_ID) == search_id:
            i.returnbook()
            return

    print("Book not found.")


while True:
    print("Library management program")
    print("1.Display All Book")
    print("2.Search for a Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. exit")

    choice = input("Enter your choice:")

    if choice == "1":
        displayall_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Loop stopped")
        break

    else:
        print("Invalid choice, Try again")
