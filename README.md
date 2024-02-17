# Global-AI-Hub-Akbank-Python-Bootcamp-Library-Management-System

This Python script implements a simple library management system where users can list books, add books, or remove books from a library. The system operates through a command-line interface (CLI) where users can input their desired actions.

## How to Use

To use the library management system, follow these steps:

1. **Run the Script**: Execute the Python script (`library_management.py`).

2. **Menu Navigation**: Upon running the script, a menu will be displayed, prompting the user to choose from the following options:

    - **List Books (Option 1)**: Lists all the books currently available in the library.
    - **Add Book (Option 2)**: Adds a new book to the library.
    - **Remove Book (Option 3)**: Removes a book from the library.
    - **Quit (Option q)**: Exits the program.

3. **Input Choices**: Enter the corresponding option number or 'q' to quit the program.

### Features

- **Listing Books**:
    - The system displays all the books currently available in the library, showing their titles and authors.
    - If there are no books in the library, it will display a message indicating the same.

- **Adding Books**:
    - Users can add new books to the library by providing the title, author, release year, and number of pages for the book.
    - It ensures that the title of the book is unique within the library. If the entered title already exists, it prompts the user to enter a different title.

- **Removing Books**:
    - Users can remove books from the library by specifying the title of the book they wish to remove.
    - If the book exists in the library, it will be removed, and a confirmation message will be displayed.

- **Input Validation**:
    - The system validates user input to ensure it corresponds to the expected data type (e.g., integer for release year and number of pages).

## Code Overview

The script consists of the following components:

- **Library Class**:
    - The `Library` class represents the library and provides methods for listing, adding, and removing books.
    - It uses a file (`books.txt`) to store information about the books.

- **Menu Display and User Interaction**:
    - The script displays a menu to the user and processes user input to perform the desired actions.

- **Input Validation**:
    - It includes a method within the `Library` class to validate user input for certain data types.

## Dependencies

The script has no external dependencies beyond the Python standard library.

## File Structure

- `library_management.py`: Contains the main Python script implementing the library management system.
- `books.txt`: Text file used to store information about the books in the library.

## Compatibility

The script is written in Python and should be compatible with Python 3.x versions.

## Conclusion

This library management system provides a simple way to manage books in a library through a command-line interface. Users can list, add, and remove books with ease, making it a practical tool for basic library management tasks.
