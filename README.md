#Library Management System Project in Python  

###In this project you can:  
####List available books:   
View a list of all books in the library.  
####Add new books:   
Enter book details (title, author, release year, number of pages) to add them to the library's catalog.  
####Remove books:   
Search for and remove books from the library's catalog.  
####Input validation:   
Ensures correct book title input during removal.  
####Error handling:   
Handles potential issues like missing books or invalid choices.  
  
##Code Structure:  
###Library class:    
'''
__init__(self):   
'''
Initializes the class, opening the text file in append and read+write mode.  
'''
__del__(self):
'''
Ensures the file is closed properly upon object destruction.  
'''
listBooks(self):
'''
Reads book information from the file, displays it in a formatted manner, and handles the case of no books found.  
'''
addBook(self):
'''
Prompts the user for book details, validates the title for uniqueness, and writes the new book information to the file.  
'''
removeBook(self):
'''
Prompts the user for the book title to remove, searches for it in the file, and updates the file content if found. Handles cases of not finding the book or invalid input.    
  
###Main function:  
-Creates a Library object instance.  
-Presents a menu to the user with options for listing, adding, and removing books, along with an exit option.  
-Based on the user's choice, calls the corresponding methods from the Library class.  
-Handles invalid input by prompting the user to enter a valid choice.  
