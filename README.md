# Library Management System Project in Python  

## In this project you can:  
List available books: View a list of all books in the library.  
Add new books: Enter book details (title, author, release year, number of pages) to add them to the library's catalog. 
![adding a book example](https://private-user-images.githubusercontent.com/108370783/306053614-23ca6b53-dac3-40d2-be5c-0c55d3610bbd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDgzNzA5MTYsIm5iZiI6MTcwODM3MDYxNiwicGF0aCI6Ii8xMDgzNzA3ODMvMzA2MDUzNjE0LTIzY2E2YjUzLWRhYzMtNDBkMi1iZTVjLTBjNTVkMzYxMGJiZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxOVQxOTIzMzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNmUyOWRjMDgzZWQwZDAzMjFkZmRjMWE5MTM2ZDg1YTEyNjM3NWZlMmMyNjQxMmFhMzg3OTMwOWU2YTI2NmJhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.6ofxqkPRwsJvN6MPG0eYV98Bxvwcg5KugzXxepcbDWk)  
![bookstxt](https://private-user-images.githubusercontent.com/108370783/306053819-2f0ec2ea-25af-4ffd-b711-1929dfdf6ebf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDgzNzA2ODcsIm5iZiI6MTcwODM3MDM4NywicGF0aCI6Ii8xMDgzNzA3ODMvMzA2MDUzODE5LTJmMGVjMmVhLTI1YWYtNGZmZC1iNzExLTE5MjlkZmRmNmViZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxOVQxOTE5NDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lYWEyYTkyN2E5N2M0ZDI4ZTFjMGE4OWYzNmRhNmY2YWEzNTNkMjAwMzU2YjRjMzVhOTQ3OWNiYTUxODVmNjZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.1R2ss0_DxgANf0U79qQvyIW-sya0s9I6RWLT99ijmQQ)
Remove books: Search for and remove books from the library's catalog.  
![removing a book example](https://private-user-images.githubusercontent.com/108370783/306053774-24c66de7-6250-4af7-9dec-dc3cd9b5920d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDgzNzA4NjEsIm5iZiI6MTcwODM3MDU2MSwicGF0aCI6Ii8xMDgzNzA3ODMvMzA2MDUzNzc0LTI0YzY2ZGU3LTYyNTAtNGFmNy05ZGVjLWRjM2NkOWI1OTIwZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxOVQxOTIyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hODcwZTFkMTQ4MmQwZjQzY2FjYjczMzJjYzY3MTJlMzY2MjczNTJmYWUyZjdkNmQxYjdmZWUyYmVlZGZmNTdhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Lmi-AH7bebH5Q5-VClbcbzF6q5Wd5wMFY2qHPdlw0co)  
Input validation: Ensures correct book title input during removal.  
Error handling: Handles potential issues like missing books or invalid choices.  
  
## Code Structure:  
### Library class:    
`__init__(self):` Initializes the class, opening the text file in append and read+write mode.  
`__del__(self):'`Ensures the file is closed properly upon object destruction.  
`listBooks(self):`Reads book information from the file, displays it in a formatted manner, and handles the case of no books found.  
`addBook(self):`Prompts the user for book details, validates the title for uniqueness, and writes the new book information to the file.  

  
### Main function:  
-Creates a Library object instance.  
-Presents a menu to the user with options for listing, adding, and removing books, along with an exit option.  
-Based on the user's choice, calls the corresponding methods from the Library class.  
-Handles invalid input by prompting the user to enter a valid choice.  
