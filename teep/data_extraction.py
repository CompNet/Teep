# 1. Data retrieval:
# a. Locate the .ncx file.
# Create a function with the code: f1
# We will create a function using our code.
# Input: the input folder (folder1a).
# Output: our two data dictionaries; it also populates the output folder (folder_exit1).
# We could technically run our code on the same input folder as many times as we like, though it would be an unnecessary waste of computational resources.
# However, the resulting files will always be the same. Output folders are not recreated if they already exist.
# The files themselves are overwritten each time.

# Imports
# For opening the epub folder
from pathlib import Path

# For handling epubs
from ebooklib import epub

# For parsing XML/XHTML
from bs4 import BeautifulSoup

# For file creation
import os

# Imports
import zipfile


# Function to extract the name from the path, removing any trailing '/' or '#'
def detectsalahhashtag(name1):
    # Find the index of the last "#"
    # Initialize to -1; if not found, it remains -1
    l1b_1 = -1
    # Iterate through the string name1
    for ll1b_1 in range(len(name1)):
        if name1[ll1b_1] == "#":
            l1b_1 = ll1b_1
    # Extract the file name if a "#" was found
    if l1b_1 != -1:
        # Slice up to l1b_1 to exclude the "#"
        way1b_1 = name1[:l1b_1]
    # Otherwise, keep the path name (the path is the file name)
    else:
        way1b_1 = name1
    # Extract the file name
    # Need to get the last component of the path after the final "/"
    # Find the index of the last "/"
    # Initialize to -1; if not found, it remains -1
    j1b = -1
    # Iterate through the string way1b_1
    for kk1b in range(len(way1b_1)):
        if way1b_1[kk1b] == "/":
            j1b = kk1b
    # Extract the file name if a "/" was found
    if j1b != -1:
        # way1b_1[j1b+1:] Afin du coup d'éviter le "/" en j1b.
        name_file1b = way1b_1[j1b + 1 :]
    # Otherwise, we keep the path name. The path is essentially the file name.
    else:
        name_file1b = way1b_1
    return name_file1b


# Function to determine if we are dealing with an .ncx or a nav.xhtml file: fncxornav
def fncxornav(content1, name_full1):
    # Variable to indicate if an ncx has been found:
    ncx = 0

    # Check if there is an .ncx file inside
    try:
        # Retrieve the ncx ID:
        # Using BeautifulSoup's XML parser
        soup = BeautifulSoup(content1, "xml")
        # Retrieve the "toc" attribute from the "spine" tag
        tag1a = soup.select_one("spine")
        assert not tag1a is None
        att1a = tag1a.get("toc")
        # We don't expect to find a nav.xhtml reference in the spine here.
        # That would imply following the EPUB3 standard, which abandoned the spine attribute.
        # If not found, we assume it is "ncx"
        if att1a is None:
            att1a = "ncx"
        # Retrieve the tag where the ID matches att1a
        # 1. Look for the tag with id = att1a
        # CSS syntax: tag[attribute='value']
        tag1a = soup.select_one("[id =" + att1a + "]")  # type: ignore
        assert not tag1a is None
        # Retrieve the value of the "href" attribute from this tag
        # This gives us the path to the .ncx file
        pathncx1a = tag1a.get("href")
        ncx = 1
        # Indicate that the .ncx file has been found for this book
        print("a .ncx for the book:" + name_full1)

    except Exception:
        # Indicate that no .ncx file was found for this book
        print("no .ncx for the book:" + name_full1)

    # Check if there is a nav.xhtml
    # How to do it?
    # To check for a nav.xhtml:
    # Look for an element with an 'id' attribute equal to "toc"
    try:
        # We know how to do this
        # Retrieve the nav ID:
        # Using BeautifulSoup's XML parser
        soup = BeautifulSoup(content1, "xml")
        # Retrieve the tag that has "toc" as its 'id' attribute
        try:
            # 1. Look for the tag with id="toc"
            # CSS syntax: tag[attribute='value']
            tag1a = soup.select_one('[id = "toc"]')
            assert not tag1a is None
            # From this tag, retrieve the value of the 'href' attribute
            # This gives the path to the nav.xhtml file
            pathnav1a = tag1a.get("href")
            # Indicate that a nav file other than .ncx was found for this book
            print("a nav.xhtml for the book:" + name_full1)
        # Otherwise, try:
        # Retrieve the tag that has "nav" as its 'id' attribute
        except:
            try:
                # 1. Look for the tag with id="nav"
                # CSS syntax: tag[attribute='value']
                tag1a = soup.select_one('[id = "nav"]')
                assert not tag1a is None
                # Retrieve the attribute value for the href attribute from this tag
                # This gives us the path to the nav.xhtml file
                pathnav1a = tag1a.get("href")
                # Indicate that a nav file other than the .ncx was found for this book
                print("a nav.xhtml for the book:" + name_full1)
            except Exception:
                # Indicate that no nav file other than the .ncx was found for this book
                print("no nav with id: nav")

        # Note: sometimes the toc attribute points to the .ncx file. In that case, it was found in the spine (handled earlier).
        # That is why we stop here if we have already found something for the .ncx.

    except Exception:
        # Indicate that no nav file other than the .ncx was found for this book
        print("no nav.xhtml for the book:" + name_full1)

    # If both an .ncx and a nav.xhtml (or similar) file are found, return the .ncx path:
    # Or if only the .ncx exists
    if ncx == 1:
        pathfinal1a = pathncx1a
    # If the .ncx is missing, the other one is the final path
    else:
        pathfinal1a = pathnav1a

    # We also need the ncx:
    return pathfinal1a, ncx


# Function to extract the name from the path, removing the part after the #
def detecthashtag(name1_1):
    # Find the index of the last "#": l1b_2
    # Initialize to -1; if no "#" is found, the value remains unchanged.
    l1b_2 = -1
    # Iterate through the string name1_1.
    for ll1b_2 in range(len(name1_1)):
        if name1_1[ll1b_2] == "#":
            l1b_2 = ll1b_2
    # Extract the file name if a "#" was found.
    if l1b_2 != -1:
        # Slice up to l1b_2 to exclude the "#" itself.
        way1b_2 = name1_1[:l1b_2]
    # Otherwise, keep the original path name (meaning the path is the file name).
    else:
        way1b_2 = name1_1
    return way1b_2


def extract_html(input_dir: Path, output_dir: Path) -> tuple[dict, dict, list, list]:
    # List of bad books
    L_bad_books = []
    # Create dictionaries:
    dic1 = {}
    dic2 = {}
    # List of file names without extensions
    L_files1a = []
    # Need to open all the epub folders
    # (We know how to do this)
    # Select the folder containing the files
    # Retrieve the folder:
    # Retrieval
    # The folder
    # Open this folder
    # Iterate through the files inside
    # Retrieve the files:
    # To be absolutely sure, retrieve only epub files
    list_files1a = input_dir.glob("*.epub")
    # Iterate through the epub files:
    for file1a in list_files1a:
        # Get the full filename, including the extension
        name_full1a = file1a.name
        # Get the full filename without the extension
        name_withoutext1a = file1a.stem
        # Open each file.
        # Attempt to open it; if it's invalid, add it to the list of invalid files:

        try:
            book1a = epub.read_epub(file1a)

            # Logically, we don't create folders for invalid books, so
            # we create the folder only here:
            pathfolder1a = output_dir / name_withoutext1a
            pathfolder1a.mkdir(parents=True, exist_ok=True)

            # Retrieve the OPF file
            # Find the .opf path via the container:

            # Retrieve the container content

            # Create a tool to browse the zip file:
            # here in read mode
            with zipfile.ZipFile(file1a, "r") as z:
                # We know this path is the same for all container.xml files.
                container = z.read("META-INF/container.xml")

            # Parse the container with BeautifulSoup and retrieve the .opf path:
            # We know the path to it is always in the same location.
            # We need to go to the "rootfile" tag and retrieve the "full-path" attribute

            # Locate the "rootfile" tag

            # Initialize the XML parser, for example:
            # for HTML and XHTML: "lxml".
            # container.xml is logically XML
            soup1a = BeautifulSoup(container, "xml")

            # If we just want the tag with a specific name:
            Tag1a = soup1a.select_one("rootfile")
            assert not Tag1a is None

            # Retrieve the "full-path" attribute
            path1a = str(Tag1a.get("full-path"))
            assert not path1a is None

            # Then open the .opf file and retrieve its content using the path:

            # Create a tool to browse the zip file:
            # here in read mode
            with zipfile.ZipFile(file1a, "r") as z:
                # Find and read a file here based on its path within the folder.
                # store its content in content1a
                content1a = z.read(path1a)

            # The path to use
            pathfinal1a, ncx = fncxornav(content1a, name_full1a)

            # Moving on to 1.b.

            # Full name of the book without extension:
            name_withoutext1b = file1a.stem

            # Create the book key in dic1 and dic2
            # using the book name (from the folder) without the extension:
            dic1[name_withoutext1b] = []
            dic2[name_withoutext1b] = {}

            # Retrieve and open the file. We have the file path within the book (pathfinal1a).
            # Extract the text following the last "/" to get the filename including its extension.
            nametoc1b = detectsalahhashtag(pathfinal1a)

            # Open the file:

            # Iterate through the current book to find the file with this name:
            # We won't modify the TOC content; we just want to extract data from it.
            # In book1a:
            for item1b in book1a.get_items():
                # Remove "/" from the name: in case the TOC is in a subfolder rather than at the EPUB root.
                name_item1b = detectsalahhashtag(item1b.get_name())
                if name_item1b == nametoc1b:
                    # Retrieve its content.
                    content1b = item1b.get_content()

            # Handle two cases depending on whether the opened TOC file is .ncx or nav.xhtml
            # If it is .ncx
            if ncx == 1:
                # Retrieve data from the file using BeautifulSoup:
                # Need to retrieve all navPoint tags:
                # Initialize the XML parser for .ncx:
                # Using content1b
                soup = BeautifulSoup(content1b, "xml")
                # Retrieve all tags matching the criteria as a standard Python list:
                tags1b = soup.select("navPoint")
                # Get the total count of files (c1b):
                # c1b is the size of the tags1b list
                # because there are as many navPoints as there are files.
                c1b = len(tags1b)
                # For .ncx files, if the playOrder is None, we need to switch to a structure
                # similar to nav.xhtml, where we calculate the playOrder ourselves.
                # Or rather, we calculate it in every case; if the playOrder is None,
                # we use the value we calculated ourselves.
                # Initialize playOrder to 1.
                myPlayOrder1b = 1
                # We can then iterate through them like any standard Python list.
                # b1b represents the current navPoint tag.
                for b1b in tags1b:
                    # For each file:
                    # Set the playOrder (we no longer retrieve it from the file, as it is often unreliable).
                    # We need to generate a fallback playOrder ourselves.
                    Current_playorder = myPlayOrder1b
                    # Increment for the next file:
                    myPlayOrder1b += 1
                    # Get the file path:
                    # It is located within the 'content' sub-tag.
                    # Find the 'content' sub-tag:
                    tag_content1b = b1b.find("content")
                    assert not tag_content1b is None
                    # Get the 'src' attribute:
                    path_file1b = tag_content1b.get("src")
                    # Remove the part after the '#' if it exists.
                    # (Remove only the '#', not the '/')
                    name_file1b = detecthashtag(path_file1b)

                    # Iterate through the book's items looking for a file with this name
                    # In the book: book1a
                    for item1b in book1a.get_items():
                        if item1b.get_name() == name_file1b:
                            # Retrieve its content
                            content_1b = item1b.get_content()

                    # Go to the output folder: "folder_exit1/"+name_withoutext1b
                    # Create a file named after the playorder: playorder1b
                    folder1b = "folder_exit1/" + name_withoutext1b
                    # File name
                    # We assume we will always use the playorder we generated ourselves
                    name_file_final1b = str(Current_playorder)
                    path_full1b = os.path.join(folder1b, name_file_final1b) + ".html"
                    # 'w' (write) mode creates the file if it doesn't exist or overwrites it if it does
                    with open(path_full1b, "wb") as f1b:
                        # Write the content (content_1b) into it
                        f1b.write(content_1b)
                    # Done
                    # Add info about this file to dic1: entry A's text and file B.b's name
                    # Retrieve A
                    # Access b1b's child tag, then the navLabel tag
                    tag_navLabel1b = b1b.navLabel
                    assert not tag_navLabel1b is None
                    # Then access its child: "text"
                    tag_text1b = tag_navLabel1b.find("text")
                    assert not tag_text1b is None
                    # Retrieve the content value from it
                    A1b = tag_text1b.get_text()
                    # Retrieve B.b
                    Bb1b = detectsalahhashtag(name_file1b)
                    # We put them in a list and add this list to dictionary dic1.
                    # We look for the key: the book title without the extension (name_withoutext1b).
                    # We then append [A1b, Bb1b] to the value associated with this key.
                    dic1[name_withoutext1b].append([A1b, Bb1b])
                    # We populate dic2.
                    # The key is the original book title—the title of its EPUB folder.
                    # Without the extension, of course: name_withoutext1b.
                    # For each book key, we have a dictionary where the keys are the files.
                    # The keys are their titles (i.e., the navPoints), and the values ​​are lists:
                    dic2[name_withoutext1b][Current_playorder] = [
                        c1b,
                        Bb1b,
                        Current_playorder,
                    ]
                # Add the filename without the extension (name_withoutext1a) to the list of filenames without extensions (L_files1a)
                L_files1a.append(name_withoutext1a)

            # If it is nav.xhtml (i.e., the 'else' case):
            else:
                # We have the content: content1b.
                # We identify each file using BeautifulSoup:
                # We create a parser for XHTML.
                # Initialize the parser as XML ("xml").
                soup = BeautifulSoup(content1b, "xml")
                # We access the first <ol> tag; we only want the first one.
                # To select tags by a specific name (e.g., 'ol'):
                tag1b = soup.select_one("ol")
                assert not tag1b is None
                # We retrieve all the <li> tags within it.
                under_tags1b = tag1b.find_all("li")
                # We have the total count of files: cc1b.
                # cc1b is the size of the under_tags1b list.
                # This is because the number of navPoints matches the number of files.
                cc1b = len(under_tags1b)
                # We can then iterate through them like any Python list.
                # under_tag1b represents the current navPoint tag.
                # Initialize playOrder to 1.
                MyPlayOrder1b = 1
                # We then iterate through all these tags:
                for under_tag1b in under_tags1b:
                    # We'll use the work done on the .ncx file for everything except BeautifulSoup.
                    # In any case, we need to access the child tag:
                    under_under_tag1b = under_tag1b.a
                    assert not under_under_tag1b is None
                    # We retrieve the following:
                    # For each file:
                    # We retrieve the playorder:
                    # Since there is no playorder for the nav, we have to generate it ourselves.
                    current_playorder = MyPlayOrder1b
                    # We increment it by 1 for the next file
                    MyPlayOrder1b += 1
                    # We get the file path:
                    # We need the href attribute.
                    path1b = under_under_tag1b.get("href")
                    # We need to remove the part after the # if it exists, as well as any slashes in the name,
                    # to avoid issues with slashes and path origins.
                    name_file1b = detectsalahhashtag(path1b)

                    # We search the book's folder for a file with this name
                    # In the book: book1a
                    for Item1b in book1a.get_items():
                        # We remove slashes from the name to avoid issues with slashes and path origins.
                        name_item1b_1 = detectsalahhashtag(Item1b.get_name())
                        if name_item1b_1 == name_file1b:
                            Content1b = Item1b.get_content()
                    # Navigate to the exit folder: "folder_exit1/"+name_withoutext1b
                    # Create a file named after the playorder: current_playorder
                    Folder1b = output_dir / name_withoutext1b
                    # File name
                    Name_file_final1b = str(current_playorder)
                    Path_full1b = os.path.join(Folder1b, Name_file_final1b) + ".html"
                    # 'w' mode (write) creates the file if it doesn't exist or overwrites it if it does.
                    # It's binary data, so use 'wb'
                    with open(Path_full1b, "wb") as F1b:
                        # Write the content (content1b) into it
                        F1b.write(Content1b)
                    # Done
                    # Add info about this file to dic1: the text from entry A and the file name B.b.
                    # Retrieve A.
                    # This is the text from tag 'a'—specifically: under_under_tag1d
                    AA1b = under_under_tag1b.get_text()
                    # Retrieve B.b.
                    BBb1b = detectsalahhashtag(name_file1b)
                    # Put them in a list and add that list to dictionary dic1.
                    # Target the key: the book title without extension (name_withoutext1b).
                    # Append [A., B.b.] to the value associated with this key
                    dic1[name_withoutext1b].append([AA1b, BBb1b])
                    # Populate dic2.
                    # The key is the original book title (the name of its epub folder).
                    # Without the extension, of course: name_withoutext1b
                    # For each book key, there is a dictionary where the keys are the files.
                    # The keys are their titles—i.e., the navpoints. And the values ​​in list form:
                    dic2[name_withoutext1b][current_playorder] = [
                        cc1b,
                        BBb1b,
                        current_playorder,
                    ]
                # Add the filename without the extension (name_withoutext1a) to the list of filenames without extensions (L_files1a)
                L_files1a.append(name_withoutext1a)

        except Exception:
            # Add the full file name to the list of bad books, prefixed with: ""This file does not comply with the EPUB 2 and EPUB 3 standards: "
            L_bad_books.append(
                "This file does not comply with the EPUB 2 and EPUB 3 standards: "
                + file1a.name
            )

    # Return the dictionaries, the list of bad books, and the list of file names without extensions (L_files1a)
    return dic1, dic2, L_bad_books, L_files1a
