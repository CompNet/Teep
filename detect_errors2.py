# 2.1 

# Imports:
# For file management:
from pathlib import Path
import os
# For natural sorting
from natsort import natsorted
# Import for the project path
from criterias import path_project

# Main function that scans the folders of folder_exit2
def f21(folder_exit2,folder_exit3,dic1, dic2, list_bad_books, L_name_books_withoutext):
    # We're going to look for the way to folder_exit2: 
    path = Path(path_project+folder_exit2)
    # Locate folder_exit2
    # Extract all subdirectories from it
    # The paths
    l_under_folders = [f.path for f in os.scandir(path) if f.is_dir()]
    # the names:
    l_names_under_folders = [f.name for f in os.scandir(path) if f.is_dir()]
    # But the implementation is poor
    l_under_folders = [ Path(d) for d in l_under_folders]
    # We iterate through all the folders
    for k in range(len(l_under_folders)):
        # For each folder:
        # Its path:
        under_folder = l_under_folders[k]
        # Its name:
        name_book = l_names_under_folders[k]
        print(name_book)
        # We use a for loop to iterate through the folder.
        # This allows us to retrieve all the files.
        # under_folder path
        path_under_folder = under_folder
        # We retrieve the list of files:
        list_files = os.listdir(path_under_folder)
       # Sort the list
        list_files = natsorted(list_files)
        # Store the contents in a list.
        # The list:
        l_contents = []
        # Iterate through the files to populate the list
        # Create the path for the current subfolder:
        path_under_folder = Path(path_under_folder)
        for file in list_files:
            # Point to the file
            list_file = path_under_folder.glob(file)
            for file_1 in list_file:
                # Retrieve the content
                with open(file_1, "r", encoding="utf-8") as f:
                    content = f.read()
                # Add it to the list
                l_contents.append(content)
        # Set the compteur to True
        compteur = True
        # Iterate through the list l_contents up to len(list)-2
        for k in range(len(l_contents)-2):
            # Check if the content matches the next two items
            if l_contents[k] == l_contents[k+1] == l_contents[k+2] and fvide21(l_contents[k]):
                # If so:
                dic1, dic2, list_bad_books, L_name_books_withoutext, name_book = fsupprime21(dic1, dic2, list_bad_books, L_name_books_withoutext, name_book)
                # Set the compteur to False because the book should not be transferred
                compteur = False
                # Exit the loop to reduce complexity
                break
        # If the loop full without the condition being met, transfer the book; otherwise, do nothing:
        if compteur == True:
            # Perform the transfer:
            ftransfer21(name_book, folder_exit2, folder_exit3)
    return dic1, dic2, list_bad_books, L_name_books_withoutext
            

# Function that detects if the file is empty: fvide21.
# Returns True if the file is not empty.
def fvide21(content):
    if content == "":
        return False
    return True

# Function that removes the book from dic1, dic2, and L_name_books_withoutext: fsupprime21
# And this function also adds it to: list_bad_books
def fsupprime21(dic1, dic2, list_bad_books, L_name_books_withoutext,name_book):
    L_name_books_withoutext = [book for book in L_name_books_withoutext if book != name_book]
    list_bad_books.append("The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "+name_book)
    dic1 = {book: list for book, list in dic1.items() if name_book != book}
    dic2 = {book: dictionary for book, dictionary in dic2.items() if name_book != book}
    return dic1, dic2, list_bad_books, L_name_books_withoutext,name_book

# Function to transfer the book folder to folder_exit3: ftransfer21. It takes the book name as an argument.
# And the input and output folders: folder_exit2, folder_exit3
def ftransfer21(name_book2, folder_exit2, folder_exit3):
    # Get the path for folder_exit2:
    path2 = Path(path_project + folder_exit2)
    # Locate folder_exit2
    # Extract just the specific folder
    # Its path:
    l_under_folders2 = [f.path for f in os.scandir(path2) 
                        if f.is_dir() and f.name == name_book2]
    # But the implementation is flawed
    l_under_folders2 = [ Path(d) for d in l_under_folders2]
    # Iterate through all the folders
    for under_folder2 in l_under_folders2:
        # Create the corresponding version in folder_exit3
        # Define the path of the folder you want to create
        # For example: "parent_folder/new_folder"
        path_under_folder3 = Path(path_project+folder_exit3+"/"+name_book2)
        # Create the folder
        # parents=True: also creates parent folders if they do not exist
        # exist_ok=True: does not raise an error if the folder already exists
        path_under_folder3.mkdir(parents=True, exist_ok=True)   
        # Use a for loop to iterate through the folder in order.
        # Retrieve all the files:
        # Path of the subfolder
        path_under_folder2 = under_folder2
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
            path_full = os.path.join(path_under_folder3, name_file2) 
            # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does. 
            with open(path_full, 'w', encoding='utf-8') as f: 
                f.write(content)
