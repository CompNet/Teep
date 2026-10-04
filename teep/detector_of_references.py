from teep.config import TeepConfig

"""Next, we move to the detector that identifies chapters, prologues, and epilogues. We use A and B.b:
the entry text (A) and the filename (B.b).
For the 88% of books with identified entries, we retrieve the relevant files
using a simple detector:
We avoid a generic 'chapter' detector, as book titles might contain that word—it's too broad.
We implement a simple approach: we need to detect 'chapter' in all its forms.
The same applies to 'epilogue' and 'prologue'.
Regarding the word criteria used: we need to externalize them.
We create these variables in a separate file: `criteria.py`
And then import them into the main code file.

Alternatively, as a preliminary step:
for an approach using the `.ncx` file:
We can retrieve all entries where the text is simply a 1- or 2-digit number, and/or—at the book level—
where, when strung together, they form a sequence of numbers within the `.ncx`.
We assume there is normally only one single sequence of numbers per TOC; therefore, we
only need to detect that one sequence.

For the global function:
Inputs: `dictionary1` (using the original book title as the key) and `L_name_books_withoutext` (a list of book names without extensions—
specifically, the name of the ePub folder, excluding the extension).
Books have a list as their value, where we store A and B.b for each file:
the entry text (A) and the filename (B.b).
A file's A and B.b values ​​are stored at the list index corresponding to its name (minus 1).

Desired output: for each book detected as containing chapters, a `dic3` structure:
dictionary: book name -> nested dictionary keyed by filename -> value of 0 or 1. ...whether or not it is a chapter.
"""


# We will create specific functions for each detection task:

# A function to detect terms A and B.b. individually: f1détec3
# Our function takes the following as input: the text from A and the filename B.b.
# It returns True if a reference to the words "chapter," "prologue," or "epilogue" is detected in either A or B.
# Otherwise, it returns False.
# The conditions we will examine are:
# Using English as an example:
# If "chapter," "epilogue," or "prologue" is found in the filename.
# We then convert the text to lowercase and check
# if "chapter," "epilogue," or "prologue" is detected.


# And in this case, we need to set it to -1.
# We fill in the if statements in the code:
def f1détec3(A, Bb, config: TeepConfig):
    # We create a list containing A and Bb
    L_3 = [A, Bb]
    # We iterate through this list
    for text3 in L_3:
        # We retrieve the text and convert it to lowercase:
        Text3 = text3.lower()
        # We use an if statement for each criterion
        # We handle the -1 cases first because they exclude the subsequent ones
        if config.c_copyright in Text3:
            return -1
        if config.c_epigraph in Text3:
            return -1
        if config.c_glossary in Text3:
            return -1
        if config.c_about_author in Text3:
            return -1
        if config.c_about_publisher in Text3:
            return -1
        if config.c_also_by in Text3:
            return -1
        # With: if .. in : return True
        if config.c_chapter in Text3:
            return True
        if config.c_prologue in Text3:
            return True
        if config.c_epilogue in Text3:
            return True
    # After iterating through the entire list without returning True,
    # we return False.
    return False


# A function to detect chapters within the entire book.
# Python algorithm:
# Function name: f2détec3
# Input: the list for each book.
# A list of sub-lists containing 'A.' and 'B/b' markers for each file.
def f2détec3(L_book3):
    # Variables to create
    # We create two lists:
    # One: the first elements of each sub-list. LL3
    LL3 = [k13 for [k13, k23] in L_book3]
    # A second one: the second elements of each sub-list. LLL3
    LLL3 = [k23 for [k13, k23] in L_book3]
    # We put them into ML3.
    ML3 = [LL3, LLL3]
    # Lj3: the list of indices j3 indicating whether they are chapters or not (0 or 1).
    # Initially 0, with length len(L_book3)
    Lj3 = [0 for k3 in L_book3]
    # The code itself:
    # We iterate through ML3. We take ml3
    for ml3 in ML3:
        # a3: whether a 1 was detected previously. Value: True or False.
        a3 = False
        # b3: whether we are on the right track. Value: True or False.
        b3 = False
        # c3: previous numeric value from the text
        c3 = 0
        # jj3: value of the index where a 1 is found and needs to be stored.
        jj3 = 0
        # We iterate through ml3. j3
        for j3 in range(len(ml3)):
            # We check if b3 is True
            if b3 == True:
                # In this case, we simply check if the text (ml3[j3]) is indeed the next number—specifically c3 + 1.
                if ml3[j3] == str(c3):
                    # And we increment c3
                    c3 += 1
                    # We also store the text index j3 in Lj3 by setting it to 1.
                    Lj3[j3] = 1
            # Otherwise: we check if a3 is True
            elif a3 == True:
                # Check if the value at the current position is "2".
                if ml3[j3] == "2":
                    # If so, we are on the right track.
                    # Set c3 to 3.
                    c3 = 3
                    # and b3 to True.
                    b3 = True
                    # Store the current index j3 in Lj3 by setting it to 1.
                    Lj3[j3] = 1
                    # Store the previous index jj3 in Lj3 by setting it to 1 (since we now know it is valid).
                    Lj3[jj3] = 1
                # If it is not "2", reset a3 to False.
                else:
                    a3 = False
            # Otherwise: check if there is a "1".
            else:
                # If the digit "1" is detected on its own.
                if ml3[j3] == "1":
                    # Set a3 to True.
                    a3 = True
                    # Store the current index j3 in jj3 to keep it in memory while waiting for the "2".
                    jj3 = j3
    # Finally, upon exit: Lj3 contains a "1" at the indices corresponding to chapter lines.
    return Lj3


# Final function to call them:
def build_dic3(dic1: dict, L_name_books_withoutext3: list, config: TeepConfig) -> dict:
    # Create the final dictionary: dic_3
    dic_3 = {}
    # Iterate through L_name_books_withoutext3
    for name_book3 in L_name_books_withoutext3:
        # Create a dictionary entry for the book in dic_3:
        dic_3[name_book3] = {}
        # Retrieve the corresponding value from dict for each book
        L_3 = dic1[name_book3]
        # The value is a list (L_3) containing pairs of [A., B.b.] for each file.
        # L_3 = [[A., B.b.], ..., [A., B.b.]]
        # Where A. is the entry text and B.b. is the file name. # Then, pass L_3 into f2détec3(L_book3)
        L_result3 = f2détec3(L_3)

        # Next, iterate through L_3 to call f1détec3([A.,B.b.])
        for kk3 in range(len(L_3)):
            # L_3[kk3] = [A.,B.b.]
            # This corresponds to the file's name: a file's A. and B.b. values ​​relate to the list index
            # (index + 1 = name)
            # Thus: name_file3 = kk3 + 1
            name_file3 = kk3 + 1
            # And for each sub-list, pass it into: f1détec3(L_3[kk3]) = f1détec3([A.,B.b.])
            value_3 = f1détec3(L_3[kk3][0], L_3[kk3][1], config)
            # Apply the consequences
            # If True, it means at least one reference to "chapter", "prologue", etc., was found in this file
            # Or L_result3[kk3] == 1
            # So, set the value to 1 for this file in the book's sub-dictionary
            # Case where f1détec3 determines it is not a chapter
            if value_3 == -1:
                dic_3[name_book3][name_file3] = -1
            elif value_3 == True or L_result3[kk3] == 1:
                dic_3[name_book3][name_file3] = 1
            # Otherwise, set to 0
            else:
                dic_3[name_book3][name_file3] = 0

        print(name_book3)

    return dic_3
