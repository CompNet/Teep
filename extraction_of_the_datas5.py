#1. Data retrieval:
# We take the base code from step 1 and modify it linearly to ultimately achieve the desired result.
# We are not updating the comments to match our current standards.

#imports
# Keeping everything for now.
#for opening the epub folder
from pathlib import Path
#epub management
from ebooklib import epub
#parsing XML/XHTML code
from bs4 import BeautifulSoup 
#import for file creation
import os
#imports
import zipfile
# Import for the project path
from criterias import path_project

# Function to extract the filename from the path, removing any '/' or '#'
# We will keep this function as is
def detectsalahhashtag(name1):
    # Get the index of the last "#": l1b_1
    # Initialize to -1; if nothing is found, it remains unchanged.
    l1b_1 = -1
    # Iterate through the string name1.
    for ll1b_1 in range(len(name1)):
        if name1[ll1b_1] == "#":
            l1b_1 = ll1b_1
    # Extract the filename if a "#" was found
    if l1b_1 != -1:
        # Slice up to l1b_1 to exclude the "#"
        way1b_1 = name1[:l1b_1]
    # Otherwise, keep the path name (meaning the path is the filename)
    else:
        way1b_1 = name1
    # Extract the filename
    # We need to get the last component of the path after the final "/"
    # We retrieve and open the file; the file path is stored in path_file1b.
    # We simply extract the text following the last "/" to get the filename, including its extension.
    # Get the index of the last "/": j1b
    # Initialize to -1; if nothing is found, it remains unchanged.
    j1b = -1
    # Iterate through the path_file1b string.
    for kk1b in range(len(way1b_1)):
        if way1b_1[kk1b] == "/":
            j1b = kk1b
    # Extract the filename if a "/" was found.
    if j1b != -1:
    # way1b_1[j1b+1:] to skip the "/" at index j1b.
        name_file1b = way1b_1[j1b+1:]
    # Otherwise, keep the path name; this implies the path itself is the filename.
    else:
        name_file1b = way1b_1
    return name_file1b


# Function to extract the name from the path, excluding the #
# We will keep this function as is
def detecthashtag(name1_1):
    # Get the index of the last "#": l1b_2
    # Initialize to -1; if no "#" is found, it remains unchanged.
    l1b_2 = -1
    # Iterate through the string name1_1.
    for ll1b_2 in range(len(name1_1)):
        if name1_1[ll1b_2] == "#":
            l1b_2 = ll1b_2
    # Extract the file name if a "#" was found
    if l1b_2 != -1:
        # Slice up to l1b_2 to exclude the "#" itself.
        way1b_2 = name1_1[:l1b_2]
    # Otherwise, keep the path name (meaning the path is the file name).
    else:
        way1b_2 = name1_1
    return way1b_2


# Function to retrieve the OPF path:
def path_opf(pointer_file1a):
    # Retrieve the OPF
    # Find the .opf path via the container:

    # Retrieve the container content

    # Create a tool to browse the zip file:
    # here in read mode
    with zipfile.ZipFile(pointer_file1a, 'r') as z:
        # We know this path is the same for all container.xml files.
        container = z.read('META-INF/container.xml')

    # Parse the container with BeautifulSoup and retrieve the .opf path:
    # We know the path to it is always in the same location.
    # Go to the "rootfile" tag and retrieve the "full-path" attribute

    # Access the "rootfile" tag

    # Initialize the XML parser, for example:
    # "lxml" for HTML and XHTML.
    # container.xml is logically XML
    soup1a = BeautifulSoup(container, "xml")

    # If we just want the tag with a specific name:
    Tag1a = soup1a.select_one("rootfile")

    # Retrieve the "full-path" attribute
    path1a = Tag1a.get("full-path")

    # Return the .opf path:
    return path1a


# list_bad_books: list of bad books (filenames without extensions).
def f1_5(list_bad_books, folder_entry):
    # List of bad books
    # New list of bad books
    list_bad_books_1 = []
    # Create dictionaries:
    dic1_1 = {}
    dic2_1 = {}
    # List of filenames without extensions
    L_name_books_withoutext_1 = []
    # Need to open the epub folders
    # (Standard procedure)
    # Select the folder containing the files
    # Retrieve the folder:
    # Retrieval
    # The folder
    folder1a = Path(path_project + folder_entry)
    # Open this folder
    # Iterate through the files inside
    # Retrieve the files:
    # To be absolutely sure, retrieve only epub files
    liste_files1a = folder1a.glob("*.epub")
    # Iterate through the epub files:
    for file1a in liste_files1a:
        
        # Get the full filename, including extension
        name_full1a = file1a.name
        # Full book name without extension
        name_withoutext1a = file1a.stem

        # Print the name of the book currently being processed:
        print(name_withoutext1a)

        # We are only interested in books that are in list_bad_books:
        if name_withoutext1a in list_bad_books:

            # Open each file in the list.
            # Attempt to open it; if it's invalid, add it to the list of invalid files:

            try: 
                book1a = epub.read_epub(file1a)

                # Logically, we don't create a folder for invalid books, so we only create the folder here:
                # Create a folder with this name inside: folder_exit5_1
                # Define its path
                pathfolder1a = Path("folder_exit5_1/"+name_withoutext1a)
                # Create the folder
                # parents=True: also creates parent folders if they don't exist
                # exist_ok=True: does not raise an error if the folder already exists
                pathfolder1a.mkdir(parents=True, exist_ok=True)

                # Get the path to the .opf file
                path1a = path_opf(file1a)

                # Then open the .opf file and retrieve its content using the path:

                # Create a tool to navigate the zip file:
                # here in read mode
                with zipfile.ZipFile(file1a, 'r') as z:
                    # Find and read a file here using its path within the archive.
                    # store its content in content1a
                    content1a = z.read(path1a)

                # Create the book key in dic1_1 and dic_2_1
                # using the book name (without extension):
                dic1_1[name_withoutext1a] = []
                dic2_1[name_withoutext1a] = {}
                
                # First, we want to retrieve the list of spine tags:
                # Initialize the XML parser for .opf:
                # Using content1a
                soup = BeautifulSoup(content1a, "xml")
                # Retrieve the spine tag:
                tag_spine = soup.select_one('spine')
                # Retrieve all tags matching the criteria as a standard Python list:
                # We want to get a list of item tags.
                tags1b = tag_spine.find_all('itemref')

                # Then, iterate through each of these tags to find the corresponding file:
                # We have the total count of files: c1b
                # c1b is the size of the tags1b list
                # Because there are as many items as there are files.
                c1b = len(tags1b)
                # Initialize playOrder to 1.
                myPlayOrder1b = 1
                # We can then iterate through them like any Python list.
                # b1b is the current itemref tag.
                for b1b in tags1b:
                    # For each file:

                    # Retrieve the playorder: We no longer fetch it directly, as it is sometimes unreliable.
                    # We will have to generate a fallback playorder ourselves.
                    Current_playorder = myPlayOrder1b
                    # Increment by 1 for the next file
                    myPlayOrder1b += 1

                    # Determine which manifest sub-tag contains our book:
                    # Retrieve the idref from the current itemref tag:
                    idref_en_court = b1b["idref"]
                    # Retrieve the 'item' tag from the entire .opf file that has the ID: idref_en_court
                    tag_manifest = soup.find_all('item', id=idref_en_court)

                    # Get the file path:
                    # It is located within tag_manifest; specifically, it is the value of the 'href' attribute.
                    path_file1b = tag_manifest[0].get("href")

                    # Remove the part following the '#' symbol, if present.
                    # (Remove only the '#', not the '/'.)
                    name_file1b = detecthashtag(path_file1b)
                    # Search the book's folder for a file with this name.
                    # Within the book: book1a
                    for item1b in book1a.get_items():
                        if item1b.get_name() == name_file1b:
                            # Retrieve its content.
                            content_1b = item1b.get_content()
                        
                    # Navigate to the output folder: "folder_exit5_1/"+name_withoutext1a
                    # Create a file named after the playorder: playorder1b
                    # (Note: the folder path does not necessarily need to be a full system path.)
                    folder1b = "folder_exit5_1/"+name_withoutext1a
                    # File name
                    # We assume we will always use the playorder we generated ourselves.
                    name_file_final1b = str(Current_playorder)
                    path_full1b = os.path.join(folder1b, name_file_final1b)
                    # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does.
                    with open(path_full1b, 'wb') as f1b:
                        # Write the content (content_1b) into the file
                        f1b.write(content_1b)
                    # And that's it
                    # Add info about this file to dic1_1; specifically, the name of file B.b.
                    # Retrieve B.b.
                    Bb1b = detectsalahhashtag(name_file1b)
                    # Put it in a list and add that list to dictionary dic1_1.
                    # Target the key: the book title without extension (name_withoutext1a)
                    # Append [B.b.] to the value associated with this key
                    dic1_1[name_withoutext1a].append([Bb1b])
                    # Populate dic_2_1.
                    # The key is the original book title—the name of its epub folder.
                    # Without the extension, of course: name_withoutext1a
                    # For each book key, we have a dictionary where the keys are the files.
                    # The keys are the file titles (i.e., the navpoints), and the values ​​are lists:
                    dic2_1[name_withoutext1a][Current_playorder]=[c1b,Bb1b,Current_playorder]
                #Add the full name of the book without the extension (name_withoutext1a) to the list of filenames without extensions (L_files1a).
                L_name_books_withoutext_1.append(name_withoutext1a)
                
            except Exception as e:
                # Add the full filename to the list of invalid books, prefixed with: ""This file does not comply with the EPUB 2 and EPUB 3 standards:"
                list_bad_books_1.append("This file does not comply with the EPUB 2 and EPUB 3 standards: " + file1a.name) 
    
    # Return the dictionaries and the list of invalid books, along with the list of filenames without extensions: L_files1a
    return dic1_1, dic2_1, list_bad_books_1, L_name_books_withoutext_1


