# -*- coding: utf-8 -*-
"""library_management_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffuJIbXdOiGdWEJfw09XKM-AUw561PeW
"""

class Library:
  # constructor
  def __init__(self):
    self.file = open("books.txt","a+")

  # destructor closes the file
  def __del__(self):
    self.file.close()
  #when the user enters "1", list_books() function is activated
  def list_books(self):
    #go to the head of the file
    self.file.seek(0)
    #get the lines of and split a file into the list
    book_lines = self.file.read().splitlines()

    #if the list is full, split every line,print the result as book name and author
    #else, print the other condition: "there is no book in the library"
    if book_lines:
      for line in book_lines:
        book_info = line.split(",")
        print(f"Book: {book_info[0]}, Author: {book_info[1]}")
    else:
      print("There is no book in the library")

#when the user enters "2", add_book() function is activated
  def add_book(self):
    # Read the existing books from the file and create a list of books
    self.file.seek(0)
    books = self.file.readlines()
    bookList = []
    for book in books:
      book_info = book.strip().split(',')
      bookList.append(book_info)

        # Prompt the user to enter the title of the book
    while True:
      title = input("Enter the title of the book: ").capitalize()

        # Check if the entered title already exists in the list of books
      title_exists = False
      for book in bookList:
        if title == book[0]:
          print("The book is already on the list.")
          title_exists = True
          break

            # If the title doesn't exist in the list, exit the loop
      if not title_exists:
          break

    # Prompt the user to enter the author of the book
    author = input("Enter the author of the book: ").capitalize()

    # Prompt the user to enter the release year of the book
    release_year = self.get_valid_input("Enter the release year of the book: ", int)

    # Prompt the user to enter the number of pages of the book
    num_pages = self.get_valid_input("Enter the number of pages: ",int)

    # Create the book information string
    book_info = f"{title},{author},{release_year},{num_pages}\n"

    # Write the book information to the file
    self.file.write(book_info)

    # Print a success message
    print("Book added successfully.")


  def get_valid_input(self, message, data_type):
        while True:
            user_input = input(message)
            try:
                user_input = data_type(user_input)
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid value.")

  #when the user enters "3", remove_book() function is activated
  #This method removes the book name received from the user
  #from the books.txt file.
  def remove_book(self):
    #input the remove title and read the existing books
    remove_title = input("Enter the book title to remove: ")

    #go to the head of the file
    self.file.seek(0)
    #get the lines of and split a file into the list
    book_lines = self.file.read().splitlines()


    new_book_lines = []
    # for loop through each line in the book_lines list
    for line in book_lines:
      #if remove_title is not in the line
      if remove_title not in line:
        #we can append this line to the new_book_lines list
        new_book_lines.append(line)

    #go to the head of the file again
    self.file.seek(0)

    #The file contents are cleared (with truncate())
    #and the new list is written to the file.
    self.file.truncate()
    self.file.write('\n'.join(new_book_lines))

    #print the removed book
    print(f"{remove_title} book was removed from the library.")

lib = Library()


#put this inside "lib" object

menu = """  ***MENU***
  1) List Books
  2) Add Book
  3) Remove Book
  q) Quit
"""
print(menu)

# input çıkarken

while True:
  menu_input = input("Enter your choice ('q' For quit ): ")

  if menu_input == "1":
    print("List books menu is active")
    lib.list_books()
  elif menu_input == "2":
    print("Add book menu is active")
    lib.add_book()
  elif menu_input == "3":
    print("Remove book menu is active")
    lib.remove_book()
  elif menu_input == "q":
    print("Bye!")
    break
  else:
    print("Invalid enter. Try again!")
