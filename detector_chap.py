# Part 4.


# The detection functions take text as input—specifically, the file's text tokenized into words.
# This results in a Python list containing the words, along with the total number of lines in the file (excluding empty lines).
# The text is handled as a single content block.
# The output is True if the file was detected, and False otherwise.
# You can run the code on the same input folder as many times as you like, though doing so adds unnecessary computational overhead.
# However, the results for the files will remain the same. Output folders are not recreated if they already exist.
# The files themselves are overwritten each time.


# Imports
# For stemming
from nltk.stem import SnowballStemmer
# Import criterias.py
import criterias
# For creating folders:
from pathlib import Path
# For creating files:
import os
# For word tokenization:
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
# Import for the project path
from criterias import path_project

# acknowledgements function
def facknowledgements4(L_tokenized4, nb_lines4):
    # Stem all words in the text
    # Import the list of reference roots (L_roots4) from criterias.py
    L_roots4 = criterias.L_roots_acknowledgements
    # Select the language for stemming
    # Defined in criterias.py
    # Import it:
    language4 = criterias.language
    # Apply it here
    stemmer4 = SnowballStemmer(language4)
    # Counter for occurrences of text words (m4) in L_roots4: nbm4
    nbm4 = 0
    # Stem all words in L_tokenized4:
    for word4 in L_tokenized4:
        # Stem the word
        m4 = stemmer4.stem(word4)
        # Count occurrences of the stemmed word (m4) in L_roots4: nbm4
        if m4 in L_roots4:
            nbm4 += 1
    # If the number of lines is zero, return False:
    if nb_lines4 == 0:
        return False
    # Calculate: text size (number of lines) / number of occurrences of these words in the text = nbm4/nb_lines4: feature4_1
    feature4_1 = nbm4/nb_lines4
    # Define the threshold of 0.3: threshold4
    threshold4 = 0.3
    # Return True if feature4_1 >= threshold4, otherwise False
    if feature4_1 >= threshold4:
        return True
    return False


# Function for section or book titles. ftitles4
def ftitles4(L_tokenized4_1,nb_lines4_1):
    # Number of words
    n4 = len(L_tokenized4_1)
    # If less than 200 words we remove: 
    if n4 < 200:
        return True
    # Otherwise we return True
    return False


# Copyright function
# Checks if the text is less than 20 lines long and contains
# the word "copyright" (or "Copyright") and the © character.
def fcopyright4(L_tokenized4_2, nb_lines4_2):
    # Retrieve the copyright criterion and logo
    c_Copyright4 = criterias.c_Copyright
    logo_Copyright4 = criterias.logo_Copyright
    # Check if the text is less than 20 lines long:
    if nb_lines4_2 < 20: 
        # Check if c_Copyright4 or logo_Copyright4 is found in the tokens (L_tokenized4_2)
        if (c_Copyright4 or c_Copyright4.lower()) and logo_Copyright4 in L_tokenized4_2:
            return True 
    # Otherwise, return False
    return False


# Glossary function
# Takes the text as a variable as well.
def fglossary4(L_tokenized4_4, nb_lines4_4, text4):
    # Detect the word "glossary"
    # Retrieve the glossary criterion
    c_glossary4 = criterias.c_glossary
    # Check if c_glossary4 (or its lowercase version) is found in the tokens
    if (c_glossary4 or c_glossary4.lower()) in L_tokenized4_4:
        print("reference to " + c_glossary4)
        return True 
    
    # The density of ":" per line. More than 80%
    # Counter for the number of times a word in text m4 is in L_roots4: nbm4
    nbm4_1 = 0
    # Iterate through all words in L_tokenized4:
    for word4_1 in L_tokenized4_4:
        # Detect the number of times a word in text word4 is ":":
        if word4_1 == ":":
            nbm4_1 += 1
    # If the number of lines is zero, return True:
    if nb_lines4_4 == 0:
        print("number of lines is zero")
        return True
    
    # Calculate: text size (number of lines) / number of times these words appear in the text = nbm4/nb_lines4: feature4_1
    feature4_1 = nbm4_1/nb_lines4_4
    # Density of ":" per line. More than 70%
    threshold4_1 = 0.7
    # Return True if feature4_1 >= threshold4, otherwise False
    if feature4_1 >= threshold4_1:
        print("high rate of :")
        return True
    
    # If a sequence of more than 9 lines is detected where the first words are in alphabetical order.
    # We retrieve a list containing the lists of the first letters of each line (for 8 lines).
    n4 = 13
    # Why? The probabilities are (n choose 25+n) / (26**n), where n is the number of lines.
    # See Gemini and ChatGPT; the concept is easily understood through them if one wishes to learn more.
    # For n=7, it equals approximately 4 * 10**(-4).
    # This will happen roughly once every 2,000 lines.
    # For n=8, it is 6 * 10**(-5).
    # For n=9, it is 10**(-5).
    # So, once every 10,008 lines of text.
    # For n=13, it is 2 * 10**(-9).
    # This error can be considered negligible.
    # We retrieve a list containing all the first letters of the lines in text4.
    # Excluding the first letters of empty lines.
    # List: List_first_lettre
    List_first_lettre4 = []
    # Not using bash.
    list_lines4 = text4.splitlines()
    for line4 in list_lines4:
        # Check if the line exists:
        if line4:
            List_first_lettre4.append(line4[0])
    List_suite4 = []
    for k4 in range(len(List_first_lettre4) - (n4 - 1)):
        list_temporary4 = List_first_lettre4[k4:k4+n4]
        List_suite4.append(list_temporary4)
    # We iterate through this list and check if the letters are in alphabetical order.
    for under_list4 in List_suite4:
        # Exclude sequences containing digits:
        # List of digits
        l4 = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Flag variable to ensure no digits are present
        a4 = True
        for k in l4:
            if k in under_list4:
                # If a digit is found in under_list4
                # Reset the flag.
                a4 = False
        # Check for "“", "‘", or "\t" in the list:
        # These characters skew the results (e.g., multiple instances in dialogue).
        # They are still sorted alphabetically relative to letters.
        # And crucially, they are not letters!
        # Therefore, we require the absence of "“", "‘", or "\t" and that the digit flag remains True.
        if ("“" not in under_list4) and ("‘" not in under_list4) and ("\t" not in under_list4) and ('"' not in under_list4) and ('[' not in under_list4) and a4 :
            if under_list4 == sorted(under_list4, reverse=False):
                print("List of initial letters in alphabetical order:")
                print(under_list4)
                return True 
    
    # Otherwise, return False in all cases
    return False


# Regarding the publisher:
def fpublisher4(L_tokenized4_5, nb_lines4_5):
    # We place the list of reference roots in criteria.py and import it: L_roots4
    L_words_5 = criterias.L_words_publisher
    # Publisher root
    root_publisher4 = criterias.c_publisher
    # We select the language for stemming:
    # Defined in criteria.py
    # Imported here:
    language4_5 = criterias.language
    # Applied here
    stemmer4_5 = SnowballStemmer(language4_5)
    # Counter for the number of times a word from text m4 matches root_publisher4: nbm4
    nbm4_5 = 0
    # We stem all words in L_tokenized4_5:
    for word4_5 in L_tokenized4_5:
        # Stem the word
        m4_5 = stemmer4_5.stem(word4_5)
        # Detect the number of times a word from text m4_5 matches root_publisher4: nbm4_5
        if m4_5 == root_publisher4:
            nbm4_5 += 1
    # Counter for L_words_5
    nbm4_52 = 0
    for word4_52 in L_tokenized4_5:
        # Detect the number of times a word from list L_words_5 appears within a token.
        for word_référence5 in L_words_5:
            if word_référence5 in word4_52:
                nbm4_52 += 1
    # Counter for numbers
    nbm4_53 = 0
    # We desactive it:
    """
    for word4_53 in L_tokenized4_5:
        # Stem the word
        m4_53 = stemmer4_5.stem(word4_53)
        # Detect how many times a word in the text (m4_53) is a number.
        # Try to convert the token to an int; if successful, it means it was originally an integer.
        try:
            int(m4_53)
            nbm4_53 += 1
        except Exception as e:
            # Otherwise, do nothing.
            nbm4_53 = nbm4_53
    """
    # If the data above is found in about 40% of the lines, it's a match.
    # Calculate the final count for the data above:
    nb_final5 = nbm4_5 + nbm4_52 + nbm4_53
    # Why 40? A guess.
    # If the number of lines is zero, return True:
    if nb_lines4_5 == 0:
        return True
    # Calculate: number of times these words appear in the text / text size (number of lines) = nb_final5/nb_lines4_5: feature4_5
    feature4_5 = nb_final5/nb_lines4_5
    # Define the threshold as 0.4: threshold4_5
    threshold4_5 = 0.4
    # Return True if feature4_5 >= threshold4_5, otherwise False
    if feature4_5 >= threshold4_5:
        return True
    return False


# Main Function:
# Inputs: folder_exit3_1, dic2, dic3, and L_name_books_withoutext
def fprincipal5(dict2, dict3, L_name_books_withoutext):
    # Iterate through L_name_books_withoutext
    for name_book4 in L_name_books_withoutext:
        # For each book:
        # Create a folder in folder_exit4 named after the book (without the extension).
        # Define the path of the folder to be created
        # For example: "folder_parent/nouveau_folder"
        path4 = Path(path_project + "folder_exit4/" + name_book4)
        path4.mkdir(parents=True, exist_ok=True)
        # Retrieve its dictionary from dict2: maybe for use with other features later. dict_book4 = dict2[name_book4]
        dict_book4 = dict2[name_book4]
        # We iterate through its folder within folder_exit3_1
        # Retrieval: get path4_1
        path4_1 = Path(path_project+"folder_exit3_1/"+name_book4)
        # Get the files:
        list_files4 = path4_1.glob("*")
        print(name_book4)
        for file4 in list_files4:
            # For each file, check if it has already been processed using dict3
            # Get its name without the extension
            name_alone4 = file4.stem
            # Get its value from dict3: dict3[name_book4][name_alone4]
            value4 = dict3[name_book4][int(name_alone4)]
            # Then use dict2
            # Required variables: L_tokenized4, nb_lines4, text4 (representing the tokenized file text, line count, and raw text, respectively)
            # Retrieve the file text
            with open(file4, "r", encoding="utf-8") as f4:
                content4 = f4.read()
            # If in dict3 we find 0:
            if value4 == 0:
                # Then its number of lines. Without empty lines 
                # The list of lines 
                line_text4 = content4.splitlines()
                # We recover the number of non-empty lines
                nb_lines_text_withoutempty4 = 0
                for line4 in line_text4:
                    if (line4 != "") and (line4 != " "):
                        nb_lines_text_withoutempty4 +=1
                # Then we tokenize it into words
                tokenized_content4 = word_tokenize(content4)
                # We will call the different detection methods
                # True counter
                count4 = 0
                # facknowledgements4(L_tokenized4,nb_lines4)
                if facknowledgements4(tokenized_content4,nb_lines_text_withoutempty4):
                    count4 += 1
                    print("for file "+name_alone4)
                    print("detect facknowledgements4")
                # ftitles4(L_tokenized4_1,nb_lines4_1)
                if ftitles4(tokenized_content4,nb_lines_text_withoutempty4):
                    count4 += 1
                    print("for file "+name_alone4)
                    print("detect ftitles4")
                #fcopyright4(L_tokenized4_2,nb_lines4_2)
                if fcopyright4(tokenized_content4,nb_lines_text_withoutempty4):
                    count4 += 1
                    print("for file "+name_alone4)
                    print("detect fcopyright4")
                #fglossary4(L_tokenized4_4,nb_lines4_4,text4)
                if fglossary4(tokenized_content4,nb_lines_text_withoutempty4,content4):
                    count4 += 1
                    print("for file "+name_alone4)
                    print("detect fglossary4")
                #fpublisher4(L_tokenized4_5,nb_lines4_5)
                if fpublisher4(tokenized_content4,nb_lines_text_withoutempty4):
                    count4 += 1
                    print("for file "+name_alone4)
                    print("detect fpublisher4")
                # If they return True. If count4 >= 1: Then set -1 in dict3
                if count4 >= 1:
                    dict3[name_book4][int(name_alone4)] = -1
            # We check the value in dict3; if it is 0 or 1, we place the file in folder_exit4, 
            # specifically within the subfolder corresponding to its book.
            # Target path (path4):
            # File name: same name, but with the .txt extension (i.e., file4.name).
            # And we write content4 into it.
            if (dict3[name_book4][int(name_alone4)] == 0) or (dict3[name_book4][int(name_alone4)] == 1):
                path_full4 = os.path.join(path4, file4.name)
                with open(path_full4, 'w', encoding='utf-8') as f4_1: 
                    f4_1.write(content4) 
                
    return dict3


