# Calibre must be downloaded on our PC; we will then use Calibre's folders.
# We will use the Python `subprocess` module, which allows us to run other processes—i.e., programs other than Python—to execute our code.


# Imports for project management
import subprocess
import os
from pathlib import Path
import shutil
# Imports for project and Calibre paths
from criterias import path_project
from criterias import path_calibre


# 3.

# We create the function that converts an HTML file to text.
def convert_html_to_txt(input_file, name_folder_exit, folder_exit_total):
    
    try:
        # We can define an output path for the function. When creating a file,
        # we can ensure the output file has a specific name:
        # the output filename is the same as the input filename, 
        # but with .html instead of .txt at the end.
        name_file = os.path.basename(input_file).replace('.html', '.txt')
        # here, the exit path points to an exit folder
        # definition of the exit folder:
        folder_exit = Path(path_project + folder_exit_total + "/" + name_folder_exit)
        # test
        print(folder_exit.exists())
        print(name_folder_exit)
        path_exit = os.path.join(folder_exit, name_file)
        # for this function
        # 'ebook-convert': Path to the ebook-convert executable
        # On Linux/macOS, it is often in the PATH.
        # On Windows, it is generally at "C:/Program Files/Calibre2/ebook-convert.exe"
        # In our case, it is located here:
        path_ebook_convert = path_calibre
        subprocess.run([path_ebook_convert, input_file, path_exit]) 
        print(f"Conversion successful")
    # in case it fails, return the error
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


# 2. 

# Transformation function
def transformation(name_folder_entry, name_file, name_folder_exit, folder_entry_total, folder_exit_total):
    # Retrieve folder
    folder = Path(path_project + folder_entry_total + "/" + name_folder_entry)
    # Retrieve files:
    list_files = folder.glob(name_file)
    for file in list_files:
        # Create an empty folder for the file and copy it inside

        # Create the folder
        # Define the path of the folder you want to create
        # Location: C:/Users/Fichiers de Travail/stage 2A/Projet/Traitement/Traitement jeu de données 1 et 2/folder_temporary
        path = Path(path_project + "folder_temporary")
        # Create the folder: folder_temporary
        # parents=True: also creates parent folders if they don't exist
        # exist_ok=True: does not raise an error if the folder already exists
        path.mkdir(parents=False, exist_ok=False)

        # Copy our file into this folder
        # Retrieve the content: content_temporary
        with open(file, "r", encoding="utf-8") as f:
            content_temporary = f.read()
        # Copying the file
        folder_temporary = path_project + "folder_temporary"
        # File name: same as the original file above, including the extension.
        # Since there can be multiple extensions, we can't just use a generic name like 'a.html'.
        # We are resolving the issue where the system cannot handle both XHTML and HTM formats
        # by forcing the conversion of HTM and XHTML files to HTML during this copy-paste process.
        # However, we need to preserve the original file name just in case, and propagate it everywhere.
        name_old_file = file.stem
        name_file = name_old_file + ".html"
        path_full = os.path.join(folder_temporary, name_file)
        # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does.
        with open(path_full, 'w', encoding='utf-8') as f:
            # Copying the temporary content (content_temporary) into the file
            f.write(content_temporary)

        # Process it using our function
        # Convert the file to text:
        # Import the file
        # Update the path
        file = path_project + "folder_temporary/" + name_file
        convert_html_to_txt(file, name_folder_exit, folder_exit_total)
        # Then delete the folder containing the file.
        # Target for deletion: folder_temporary = "C:/Users/USER/Fichiers de Travail/stage 2A/Projet/traitement des books/folder_temporary"
        folder_to_suppress = path_project+"folder_temporary"
        shutil.rmtree(folder_to_suppress)


# 1. 

def transformation_total(folder_entry_total, folder_exit_total):
    # Iterate through folder_entry_total
    # Path to the folder containing the subfolders
    folder_parent = Path(path_project + folder_entry_total)
    # Use os.scandir to access the parent folder and retrieve only items that are directories (.is_dir())
    # This yields a list of paths for the subfolders:
    under_folders = [f.path for f in os.scandir(folder_parent) if f.is_dir()]
    # Convert to Path objects
    under_folders = [Path(d) for d in under_folders]
    # Process each subfolder
    for under_folder in under_folders:

        # Create a corresponding subfolder with the same name in folder_books_texts
        # to hold all text files in the same order.
        # Create a corresponding subfolder with the same name in folder_books_texts
        # Get the folder name
        name_folder = under_folder.name
        name_folder_without_Oceano =  name_folder
        # Create a new version in folder_books_texts
        # Define the path for the folder to be created
        # For example: "folder_parent/nouveau_folder"
        path1_under_folder = Path(path_project + folder_exit_total + "/" +name_folder_without_Oceano)
        # Create the folder
        # parents=True: creates parent folders if they do not exist
        # exist_ok=True: does not raise an error if the folder already exists
        path1_under_folder.mkdir(parents=True, exist_ok=True)

        # Iterate through under_folder:
        # Retrieve under_folder using its path: under_folder
        # Retrieval
        folder = Path(under_folder)
        # Retrieve the files:
        list_file_under_folder = folder.glob("*")
        for file in list_file_under_folder:

            # Convert each folder into a text file and place it in the corresponding subfolder (with the same name) within folder_books_texts
            # Call the transformation function:
            # It takes as arguments the name of the subfolder in folder_books_texts/ (which matches folder_entry_total) and the filename with extension to be transferred
            # i.e., name_folder and file.name
            name_file = file.name
            transformation(name_folder,name_file,name_folder_without_Oceano,folder_entry_total,folder_exit_total)