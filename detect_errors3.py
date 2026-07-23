# 3.1 

# Imports:
# For directory management:
from pathlib import Path
import os
# For word tokenization:
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
# Import for the project path
from criterias import path_project

# Main function that iterates through the directories in folder_exit3
def f31(folder_exit3,folder_exit3_1,dic1, dic2, dic3, list_bad_books, L_name_books_withoutext):
    # Get the path for folder_exit3:
    path = Path(path_project + folder_exit3)
    # Locate folder_exit3
    # Extract all subdirectories
    # The paths
    l_under_folders = [f.path for f in os.scandir(path) if f.is_dir()]
    # The names:
    l_names_under_folders = [f.name for f in os.scandir(path) if f.is_dir()]
    # But the format needs adjustment
    l_under_folders = [Path(d) for d in l_under_folders]
    # Iterate through all subdirectories
    for k in range(len(l_under_folders)):
        # For each subdirectory:
        # Its path:
        under_folder = l_under_folders[k]
        # Its name
        name_book = l_names_under_folders[k]
        print(name_book)
        # We use a for loop to iterate through the folder in order.
        # We first retrieve all the files.
        # Path of the under_folder
        path_under_folder = under_folder
        # We get the list of files:
        list_files = os.listdir(path_under_folder)
        # We iterate through the files to populate the list.
        # We create the path for the current under-folder:
        path_under_folder = Path(path_under_folder)
        # We initialize a flag (count) that is True if all files are valid, and False otherwise.
        count = True
        for file in list_files:
            # We get the filename without the extension:
            # We want to remove the .txt at the end—i.e., the last 4 characters, or file[:-4].
            # And we need to convert it to an integer.
            name_file = int(file[:-4])
            # We check if its value in dic3 is 1.
            # We retrieve the value from dic3:
            value = dic3[name_book][name_file]
            if value == 1:
                # If this is the case:
                # Locate the file
                list_file = path_under_folder.glob(file)
                for file_1 in list_file:
                    # Retrieve the content
                    with open(file_1, "r", encoding="utf-8") as f:
                        content = f.read()
                # Verify that the content returns True via fcontent31
                answer = fcontent31(content)
                # If True, do nothing and continue: count is theoretically still True
                # If False, execute fsupprime31 and stop here.
                if answer == False:
                    # Set count to False.
                    count = False
                    # Remove the book from dic1, dic2, dic3, and L_name_books_withoutext, and add it to list_bad_books
                    dic1, dic2, dic3, list_bad_books, L_name_books_withoutext = fdelete31(dic1, dic2, dic3, list_bad_books, L_name_books_withoutext, name_book)
                    # Break: exit the loop. This reduces complexity.
                    break
        # If the entire list has been traversed
        # If count == True
        if count == True:
            # Then execute ftransfer31:
            ftransfer31(name_book, folder_exit3, folder_exit3_1)

    return dic1, dic2, dic3, list_bad_books, L_name_books_withoutext


def fcontent31(content):
    # we tokenize:
    tokenized_content = word_tokenize(content)
    # Number of words
    n4 = len(tokenized_content)
    # If less than 20 words we send False: 
    if n4 < 20:
        return False
    # Otherwise we return True
    return True


# Function that deletes the book in dic1, dic2, dic3 and L_name_books_withoutext: fsupprime21 
# And this function also adds it to: list_bad_books
def fdelete31(dic1, dic2, dic3, list_bad_books, L_name_books_withoutext, name_book):
    L_name_books_withoutext = [book for book in L_name_books_withoutext if book != name_book]
    list_bad_books.append("The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "+name_book)
    dic1 = {book: list for book, list in dic1.items() if name_book != book}
    dic2 = {book: dictionary for book, dictionary in dic2.items() if name_book != book}
    dic3 = {book: dictionary for book, dictionary in dic3.items() if name_book != book}
    return dic1, dic2, dic3, list_bad_books, L_name_books_withoutext


# Function to transfer the book folder to folder_exit3_1: ftransfer3_1. It takes the book name as an argument.
# And the entry and exit folders: folder_exit3, folder_exit3_1
def ftransfer31(name_book, folder_exit3, folder_exit3_1):
    # Get the path for folder_exit3:
    path3 = Path(path_project + folder_exit3)
    # Locate the specific folder
    # Extract just the correct folder
    # Its path:
    l_under_folders3 = [f.path for f in os.scandir(path3) 
                        if f.is_dir() and f.name == name_book]
    # Convert to Path objects
    l_under_folders3 = [Path(d) for d in l_under_folders3]
    # Iterate through the folders
    for under_folder3 in l_under_folders3:
        # Create its version in folder_exit3_1
        # Define the path of the folder to be created
        # For example: "folder_parent/new_folder"
        path_under_folder3_1 = Path(path_project + folder_exit3_1 + "/" + name_book)
        # Create the folder
        # parents=True: creates parent folders as well if they don't exist
        # exist_ok=True: does not raise an error if the folder already exists
        path_under_folder3_1.mkdir(parents=True, exist_ok=True)   
        # We use a for loop to iterate through the folder in order.
        # First, we retrieve all the files:
        # Path of under_folder
        path_under_folder3 = under_folder3
        # We get the list of files:
        list_files3 = os.listdir(path_under_folder3)
        # We create the path for the current under-folder:
        path_under_folder3 = Path(path_under_folder3)
        for file in list_files3:
            # We target the file
            list_file = path_under_folder3.glob(file)
            for file_1 in list_file:
                # We retrieve the content
                with open(file_1, "r", encoding="utf-8") as f:
                    content_1 = f.read()
            # And we populate it with the content:
            # The folder path doesn't necessarily have to be a Path object, but it can be. We create a file in the path: path_under_folder3_1
            # File name
            name_file3 = file_1.name 
            path_full = os.path.join(path_under_folder3_1, name_file3) 
            # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does. 
            with open(path_full, 'w', encoding='utf-8') as f: 
                f.write(content_1)