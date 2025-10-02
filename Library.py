class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
    
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"
    
class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def show_books(self):
        print("\nBooks in the library :")
        for book in self.books:
            print(book)
    
    def find_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                return book
        return None

#Example call
library=Library()

library.add_book(Book("1984","George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

library.show_books()

#Borrow a book
'''book_to_borrow=library.find_book("1984")
if book_to_borrow:
    book_to_borrow.borrow()

library.show_books()

# Return a book
book_to_borrow.return_book()

library.show_books() '''


while True:
    print("\n1. Show books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.show_books()
    elif choice == "2":
        title = input("Enter the book title to borrow: ")
        book = library.find_book(title)
        if book:
            book.borrow()
        else:
            print("Book not found.")
    elif choice == "3":
        title = input("Enter the book title to return: ")
        book = library.find_book(title)
        if book:
            book.return_book()
        else:
            print("Book not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")





