from pathlib import Path
import os
from natsort import natsorted
import nltk

nltk.download("punkt_tab", quiet=True)
from nltk.tokenize import word_tokenize


def detect_erroneous_epubs(
    input_dir: Path,
    output_dir: Path,
    dic1: dict,
    dic2: dict,
    bad_books: list,
    L_name_books_withoutext: list,
):
    l_under_folders = [f for f in input_dir.iterdir() if f.is_dir()]
    # We iterate through all the folders
    for under_folder in l_under_folders:
        name_book = under_folder.name
        print(name_book)
        # We use a for loop to iterate through the folder.
        # This allows us to retrieve all the files.
        # We retrieve the list of files:
        list_files = os.listdir(under_folder)
        # Sort the list
        list_files = natsorted(list_files)
        # Store the contents in a list.
        # The list:
        l_contents = []
        # Iterate through the files to populate the list
        for file in list_files:
            # Point to the file
            list_file = under_folder.glob(file)
            for file_1 in list_file:
                # Retrieve the content
                with open(file_1, "r", encoding="utf-8") as f:
                    content = f.read()
                # Add it to the list
                l_contents.append(content)
        # Set the counter to True
        counter = True
        # If the book has fewer than 2 elements: there is a problem with this book.
        # Specifically, if the book has only one element:
        if len(l_contents) == 1:
            counter = False
        # If there is more than one file, we can proceed with the analysis.
        else:
            # Iterate through the list l_contents up to len(liste)-2
            for k in range(len(l_contents) - 1):
                # Check if the current content matches the next content.
                if l_contents[k] == l_contents[k + 1] and fnearlyempty21(l_contents[k]):
                    # If so:
                    dic1, dic2, bad_books, L_name_books_withoutext, name_book = (
                        fdelete21(
                            dic1,
                            dic2,
                            bad_books,
                            L_name_books_withoutext,
                            name_book,
                        )
                    )
                    # Set the counter to False, as this book should not be transferred
                    counter = False
                    # Exit the loop to reduce complexity
                    break
        # If the loop full without the condition being met, transfer the book; otherwise, do nothing:
        if counter == True:
            # Perform the transfer:
            ftransfer21(name_book, input_dir, output_dir)
    return dic1, dic2, bad_books, L_name_books_withoutext


# Function to detect if the file is nearly empty: fpresquevide21. Nearly empty means fewer than 20 words.
# Returns True if the file is not nearly empty.
def fnearlyempty21(content):
    # Tokenize:
    tokenized_content = word_tokenize(content)
    # Number of words
    n4 = len(tokenized_content)
    # If fewer than 20 words, return False:
    if n4 < 20:
        return False
    # Otherwise, return True
    return True


# Function that removes the book from dic1, dic2, and L_name_books_withoutext: fsupprime21
# And this function also adds it to: list_bad_books
def fdelete21(dic1, dic2, list_bad_books, L_name_books_withoutext, name_book):
    L_name_books_withoutext = [
        book for book in L_name_books_withoutext if book != name_book
    ]
    list_bad_books.append(
        "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "
        + name_book
    )
    dic1 = {book: list for book, list in dic1.items() if name_book != book}
    dic2 = {book: dictionary for book, dictionary in dic2.items() if name_book != book}
    return dic1, dic2, list_bad_books, L_name_books_withoutext, name_book


def ftransfer21(name_book2: str, input_dir: Path, output_dir: Path):
    """
    Transfer books from two folders
    """
    # Locate folder_exit2
    # Extract just the specific folder
    # Its path:
    l_under_folders = [
        f for f in input_dir.iterdir() if f.is_dir() and f.name == name_book2
    ]
    # But the implementation is flawed
    l_under_folders = [Path(d) for d in l_under_folders]
    # Iterate through all the folders
    for under_folder in l_under_folders:
        # Create the corresponding version in folder_exit3
        # Define the path of the folder you want to create
        # For example: "parent_folder/new_folder"
        output_folder_path = output_dir / name_book2
        # Create the folder
        # parents=True: also creates parent folders if they do not exist
        # exist_ok=True: does not raise an error if the folder already exists
        output_folder_path.mkdir(parents=True, exist_ok=True)
        # Use a for loop to iterate through the folder in order.
        # Retrieve all the files:
        # Path of the subfolder
        path_under_folder2 = under_folder
        # Get the list of files:
        list_files2 = os.listdir(path_under_folder2)
        # Create the path object for the current subfolder:
        path_under_folder2 = Path(path_under_folder2)
        for file in list_files2:
            # Point to the file
            list_file = path_under_folder2.glob(file)
            for file_1 in list_file:
                # Retrieve the content
                with open(file_1, "r", encoding="utf-8") as f:
                    content = f.read()
            # And populate it with the content:
            # Create a file within the path: path_under_folder3
            # File name
            name_file2 = file_1.name
            path_full = os.path.join(output_folder_path, name_file2)
            # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does.
            with open(path_full, "w", encoding="utf-8") as f:
                f.write(content)
