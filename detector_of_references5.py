# 5. 
# Function to create our dictionary:

# We will create specific functions for each detection task:

# A function to detect terms A and B.b. individually: f1detec5
# Our function takes the following as input: input text A and filename B.b.
# It returns True if a reference to the words "chapter," "prologue," or "epilogue" is detected in A or B.
# Otherwise, it returns False.
# The conditions we will examine are:
# Using English as an example:
# If "chapter," "epilogue," or "prologue" is found in the filename.
# We then convert the text to lowercase and check
# if "chapter," "epilogue," or "prologue" is detected.
# We then need to add the necessary items to "criterias"
# and import them:
import criterias
c_chapter5 = criterias.c_chapter
c_prologue5 = criterias.c_prologue
c_epilogue5 = criterias.c_epilogue
# We also put the criterias: 
"""
copyright
epigraph 
glossary
about the author
aubout the publisher
also by
"""
c_copyright5 = criterias.c_copyright
c_epigraph5 = criterias.c_epigraph 
c_glossaryr5 = criterias.c_glossary
c_about_author5 = criterias.c_about_author 
c_about_publisher5 = criterias.c_about_publisher
c_also_by5 = criterias.c_also_by
# And in that case, we need to set it to -1.
# We fill in the 'if' statements in the code:
def f1detec5(Bb):
    # We create a list containing A and Bb
    L_5 = [Bb]
    # We iterate through this list
    for text5 in L_5:
        # We retrieve the text and convert it to lowercase:
        Text5 = text5.lower()
        # We use an 'if' statement for each criterion
        # We handle the -1 cases first because they rule out the subsequent ones
        if c_copyright5 in Text5:
            return -1
        if c_epigraph5 in Text5:
            return -1
        if c_glossaryr5 in Text5:
            return -1
        if c_about_author5 in Text5:
            return -1
        if c_about_publisher5 in Text5:
            return -1
        if c_also_by5 in Text5:
            return -1
        # Avec: if .. in : return True
        if c_chapter5 in Text5:
            return True
        if c_prologue5 in Text5:
            return True
        if c_epilogue5 in Text5:
            return True
    # After iterating through the entire list without returning True,
    # we return False.
    return False

# A function to detect chapters within the entire book.
# Python algorithm:
# Function name: f2detec5
# Input: the list for each book.
# A list of sublists containing 'A.' and 'B/b' markers for each file.
def f2detec5(L_book5):
    # Variables to create:
    # Lj5: list of indices (j5) indicating whether they are chapters (0 or 1).
    # Initialized to 0 with a size of len(L_book5).
    Lj5 = [0 for k5 in L_book5]
    # The code itself:
    # Iterate through ML5; take ml5.
    ml5 = L_book5
    # a5: tracks whether a 1 was detected previously (True or False).
    a5 = False
    # b5: indicates if we are on the right track. Value: True or False.
    b5 = False
    # c5: previous numeric value from the text
    c5 = 0
    # jj5: value of the index where a 1 is found and which must be stored in memory.
    jj5 = 0
    # Iterate through ml5 using j5
    for j5 in range(len(ml5)):
        # Check if b5 is True
        if b5 == True:
            # In this case, simply check if the text (ml5[j5]) is indeed the next number—specifically c5 + 1.
            if ml5[j5] == str(c5):
                # And increment c5
                c5+=1
                # Also store the text index j5 in Lj5 by setting it to 1.
                Lj5[j5] = 1
        # Otherwise: check if a5 is True
        elif a5 == True:
            # Check if the value at this position is 2.
            if ml5[j5] == "2":
                # If so, it means we're on the right track.
                # We set c5 = 5.
                c5 = 5
                # and b5 = True
                b5 = True
                # We also keep track of the text index, j5, in Lj5. We set it to 1.
                Lj5[j5] = 1
                # We also keep track of the previous text index—now we know it's valid.
                # jj5, in Lj5. We set it to 1.
                Lj5[jj5] = 1
            # and if it's not 2, we reset a5 to False.
            else:
                a5 = False
        # Otherwise: we check to see if there is a 1.
        else:
            # If we detect the digit 1 on its own.
            if ml5[j5] == "1":
                # We set a5 to True.
                a5 = True
                # We store the index j5 in jj5 to keep it in memory while waiting for the 2.
                jj5 = j5
    # Finally, as output: we have Lj5, containing 1s for all indices of files that are chapters.
    return Lj5


# Final function to call them:
def fabrication_dictionary5(dic1, L_name_books_withoutext5):
    # Create the final dictionary: dic3_1
    dic3_1 = {}
    # Iterate through L_name_books_withoutext5
    for name_book5 in L_name_books_withoutext5:
        # Create a dictionary entry for the book in dic3_1:
        dic3_1[name_book5] = {}
        # And for each book, retrieve its value from dic1
        L_5 = dic1[name_book5]
        # The value is a list (L_5) containing [B.b.] elements for each file.
        # L_5 = [[B.b.], ..., [B.b.]]
        # The name of the file is B.b.

        # Pass L_5 to f2detec5(L_book5)
        L_result5 = f2detec5(L_5)
        
        # Then iterate through L_5 for f1detec5([B.b.])
        for kk5 in range(len(L_5)):
            # L_5[kk5] = [B.b.]
            # We see that this corresponds to the file name: a file has its A. and B.b. corresponding to the list index (name - 1), i.e., list index + 1 = name.
            # Thus: name_file5 = kk5 + 1
            name_file5 = kk5 + 1
            # And for each sub-list, we pass it to: f1detec5(L_5[kk5]) = f1detec5([B.b.])
            value_5 = f1detec5(L_5[kk5][0])
            # We apply the consequences
            # If True, it means we found at least one reference to "chapter", "prologue", etc., in this file
            # Or L_result5[kk5] == 1
            # So, for the book's sub-dictionary instance corresponding to the file, we set the value to 1
            # Case where f1detec5 indicates it is not a chapter
            if value_5 == -1:
                dic3_1[name_book5][name_file5] = -1
            elif value_5 == True or L_result5[kk5] == 1:
                dic3_1[name_book5][name_file5] = 1
            # Otherwise, we set it to 0
            else:
                dic3_1[name_book5][name_file5] = 0
        
        print(name_book5)
    
    return dic3_1

