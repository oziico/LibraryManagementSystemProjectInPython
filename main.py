class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")
        def __del__(self):
            self.file.close()

    def listBooks(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books found.")
            return
        for book in books:
            bookInfo = book.strip().split(',')
            print(f"Book Name: {bookInfo[0]}, Author: {bookInfo[1]}")

    def addBook(self):
        bookTitle = input("Enter book title: ")
        bookAuthor = input("Enter book author: ")
        releaseYear = int(input("Enter release year: "))
        numPages = int(input("Enter number of pages: "))
        self.file.seek(0)
        existingBooks = self.file.readlines()
        for book in existingBooks:
            bookInfo = book.strip().split(',')
            if bookInfo[0] == bookTitle:
                print(f"Book '{bookTitle}' already exists.")
                return

        bookInfo = f"{bookTitle},{bookAuthor},{releaseYear},{numPages}\n"
        self.file.write(bookInfo)
        print("Book added successfully.")

    def removeBook(self):
        titleToRemove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        newBooks = []
        found = False
        for book in books:
            bookInfo = book.strip().split(',')
            if bookInfo[0] != titleToRemove:
                newBooks.append(book)
            else:
                found = True
        if not found:
            print("Book not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            for book in newBooks:
                self.file.write(book)
            print("Book removed successfully.")


def main():
    lib = Library()
    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("Q) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.listBooks()
        elif choice == "2":
            lib.addBook()
        elif choice == "3":
            lib.removeBook()
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4 or 'q' to exit.")


if __name__ == "__main__":
    main()
