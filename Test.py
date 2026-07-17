# Test: Test file for testing purposes
# 'T' suffix on variables

# Imports
# For file and folder management:
import os
from pathlib import Path 
# For plotting
import matplotlib.pyplot as plt
import numpy as np
# For natural sorting:
from natsort import natsorted
# Import for the project path
from criterias import path_project

# Note L_name_books_errors
# To avoid having to rerun the entire process each time
L_name_books_errors = ["Father_goriot", "Grave Witch (Alex Craft, #01) -- Price, Kalayna -- Alex Craft 1, 2010 -- Penguin Group (USA) --", 
"The Enchanted Castle by E. Nesbit", "_OceanofPDF.com_The_Winter_of_Our_Discontent_-_John_Steinbeck", 
"_OceanofPDF.com_Under_the_Never_Sky_Omnibus_-_Veronica_Rossi",
"_OceanofPDF.com_Wuthering_Heights_-_Emily_Bronte (1)", "_OceanofPDF.com_Yellow_Crocus_-_Laila_Ibrahim", 
"The_Martian_by_Andy_Weir", "_OceanofPDF.com_True_love_experiment_-_Christina_Lauren", 
"_OceanofPDF.com_Twisted_-_Emily_McIntire", "_OceanofPDF.com_Wicked_and_the_Wallflower_-_Sarah_MacLean"]


# Function fT1
# Function that calculates, for each book:
# How many files that are actually chapters were found
def fT1():
    # Reset dictest_1 to {}
    dictest_1 = {}
    # Iterate through the subfolders of the 'annotated' folder.
    # Retrieve the list of paths for the subfolders within the 'annotated' folder.
    # Path to the parent folder containing the subfolders
    folder_parentT = Path(path_project + "Dataset expected as output")
    # Use os.scandir to access the parent folder and retrieve only items that are folders:
    # .is_dir().
    # Obtain the list of subfolder paths:
    under_folders_pathT = [fT.path for fT in os.scandir(folder_parentT) if fT.is_dir()]
    # Obtain the list of subfolder names:
    under_folders_nameT = [fT_1.name for fT_1 in os.scandir(folder_parentT) if fT_1.is_dir()]
    # However, the path formatting needs adjustment:
    under_folders_pathT = [Path(dT) for dT in under_folders_pathT]
    # Iterate through the books in under_folders_pathT
    for k in range(len(under_folders_pathT)):
        # For each folder:
        # Create its key in dictest_1 and the associated sub-dictionary.
        # Retrieve the subfolder name
        nameT = under_folders_nameT[k]
        # Check that it is not in L_name_books_errors
        if nameT not in L_name_books_errors:
            # Indicate current location:
            print(nameT)
            # Create the key:
            dictest_1[nameT] = {}
            # Iterate through it. Retrieve all files from the folder:
            # Get the folder path:
            folder_currentT = under_folders_pathT[k]
            # Retrieve all text files
            # Get a list of them: 
            filesT = os.listdir(folder_currentT)
            # Iterate through the list:
            for fileT in filesT: 
                # For each file
                # Retrieve its content:
                # Get the file using .glob on the folder and its name: fileT
                fileT_1 = folder_currentT.glob(fileT)
                for fileT_2 in fileT_1:
                    with open(fileT_2, "r", encoding="utf-8") as fT_2:
                        contentT = fT_2.read()
                # Go to the corresponding folder within the non-annotated directory. 
                # Create the path:
                path_non_annotatedT = Path(path_project+"folder_exit4/"+nameT)
                # Retrieve all file names without extensions. 
                # Then sort them (ignoring extensions) 
                # to iterate through them in ascending order. 
                # Later, we will recreate them with their extensions 
                # to access their contents.
                files_non_annotatedT = path_non_annotatedT.glob("*.txt")
                # Extract only the names (excluding extensions) so they can be sorted numerically: 
                files_non_annotatedT = [name_avec_extT.stem for name_avec_extT in files_non_annotatedT]
                # Initialize aT to 0:
                aT = 0
                # Check if it can be found in the results folder
                for file_non_annotatedT in files_non_annotatedT:
                    # Reconstruct the full filename with its extension
                    # to access its content.
                    # Check if the content matches one of the files.
                    # Retrieve the content of the non-annotated file:
                    # Locate the file using .glob on the folder with its name: fileT
                    file_non_annotatedT_1 = path_non_annotatedT.glob(file_non_annotatedT + ".txt")
                    for file_non_annotatedT_2 in file_non_annotatedT_1:
                        with open(file_non_annotatedT_2, "r", encoding="utf-8") as fT_3:
                            contentT_1 = fT_3.read()
                    if contentT == contentT_1:
                        aT = 1
                # Store aT in dictest_1
                # Retrieve the filename with the extension (extension presence doesn't matter):
                name_fileT = fileT
                dictest_1[nameT][name_fileT] = aT
    
    return dictest_1

print(fT1())

# Function fT2
# Function that calculates the number of files found for each book.
def fT2():
    # Reset dictest_2 to {}
    dictest_2 = {}
    # Iterate through the subfolders of the 'annotated' folder.
    # Retrieve the list of paths for the subfolders found.
    # Path of the parent folder containing the subfolders
    folder_parentT = Path(path_project + "folder_exit4")
    # Use os.scandir to access the parent folder and retrieve only items that are directories:
    # .is_dir().
    # Obtain the list of subfolder paths:
    under_folders_pathT = [fT.path for fT in os.scandir(folder_parentT) if fT.is_dir()]
    # Obtain the list of subfolder names:
    under_folders_nameT = [fT_1.name for fT_1 in os.scandir(folder_parentT) if fT_1.is_dir()]
    # However, the path formatting needs correction:
    under_folders_pathT = [Path(dT) for dT in under_folders_pathT]
    # Iterate through the books in under_folders_pathT
    for k in range(len(under_folders_pathT)):
        # For each folder:
        # Create its key in dictest_2 and the associated sub-dictionary.
        # Retrieve the subfolder name
        nameT = under_folders_nameT[k]
        # Check if it is not in L_name_books_errors
        if nameT not in L_name_books_errors:
            # Indicate current processing:
            print(nameT)
            # Iterate through it. Retrieve all files from the folder:
            # Get the folder path:
            folder_currentT = under_folders_pathT[k]
            # Get all text files
            # Store them in a list:
            filesT = os.listdir(folder_currentT)
            # Create the key: the number of files in the folder
            dictest_2[nameT] = len(filesT)
    
    return dictest_2


# We will calculate accuracy, recall, and F-score for each book, as well as
# for all books combined.
# Since the relationships are linear, simply averaging the individual values ​​will suffice.
# Function to generate accuracy, recall, and F-score:
def fmetrics(dictest1, dictest2):
    # List of recall values
    L_recalls = []
    # List of accuracy values
    L_accuracys = []
    # List of F-scores
    L_fscores = []
    # X-axis:
    # List of books: keysT
    # Iterate through dictest1:
    # Get all its keys
    keysT = list(dictest1.keys())
    # Total number of books:
    nb_book = len(keysT)
    # Iterate through them:
    for keyT in keysT:
        # For each book:
        print(keyT)
        # Recall calculations:
        # Iterate through the files (i.e., their keys):
        under_keysT = dictest1[keyT].keys()
        # Number of files successfully retrieved
        nb_file_brT = 0
        # Total number of files
        nb_fileT = len(under_keysT)
        # Iterate through them:
        for under_keyT in under_keysT:
            # Retrieve the values:
            aT = dictest1[keyT][under_keyT]
            if aT == 1:
                nb_file_brT += 1
        # Calculate recall:
        recall = nb_file_brT/nb_fileT
        
        # Accuracy calculations:
        # Iterate through the files (i.e., their keys):
        # We have the number of files assigned to chapters for this book:
        nb_files = dictest2[keyT]
        # We then have the accuracy
        accuracy = nb_file_brT/nb_files

        # For F score:
        if accuracy+recall != 0:
            f_score = 2*((accuracy*recall)/(accuracy+recall))
        else:
            f_score = 0
        
        # We add them to the lists:
        # List of recalls
        L_recalls.append(recall)
        # List of accuracies
        L_accuracys.append(accuracy)
        # List of f scores
        L_fscores.append(f_score)
    
    # Initialization of totals:
    total_recall = 0
    total_accuracy = 0
    total_f_score = 0
    # Total recalls, accuracies and f scores:
    for k in range(nb_book):
        total_recall += L_recalls[k]
        total_accuracy += L_accuracys[k]
        total_f_score += L_fscores[k]
    recall_total = total_recall/nb_book
    accuracy_total = total_accuracy/nb_book
    f_score_total = total_f_score/nb_book

    return L_recalls, L_accuracys, L_fscores, recall_total, accuracy_total, f_score_total


# Test
# We have: dictest1 from fT1, representing the number of documents correctly assigned as chapters.
# And by taking the length of the keys for each book, we get the number of elements:
# That should be assigned as chapters.
# And with: dictest2 from fT2, the number of elements actually assigned as chapters.
# dictest1 = fT1()
# dictest2 = fT2()
#L_recalls, L_accuracys, L_fscores, recall_total, accuracy_total, f_score_total = fmétriques(dictest1,dictest2)
#print(L_recalls, L_accuracys, L_fscores, recall_total, accuracy_total, f_score_total)


# Order detection function.
# We will use Kendall's correlation, as it is the most precise and, crucially, works better with small samples.
# For each book, we will transform the contents into an ordering.
# For each book, we want a list of increasing numbers (0, 1, 2, 3...): l1. We start at 0.
# This corresponds to the list of annotated files considered to be in the correct order.
# Then, we create the list of numbers corresponding to the files we produced: l2. I.e., for each produced file's content:
# We look up its value in list l1 and record it in l2. This is how the second list is created.
# If the file is not found among the annotated files, it doesn't matter; we are not considering false positives here.
# Function: fcreationl
# The function needs to be rewritten. For each book, we must create l1 and l2 based on the "universe" (i.e., l1).
# Therefore, l2 needs to be reworked. It must be created with the same length as l1. We need to iterate through the annotated folder. 
# We iterate through l1. For each index corresponding to an annotated file, we check if that file exists.
# For every index in l2 (corresponding to an annotated file), the result must be either 0 (if the file does not exist) or its rank.
def fcreationl():
    # We create dictest3, using books as keys and a list of lists as values.
    # This structure contains l1—the list for the book's annotated folder—and l2—the list for the folder produced by the program.
    dictest_3 = {}
    # Iterate through the folders within the 'annotated' folder.
    # Retrieve the list of paths for the subfolders found.
    # Path to the parent folder containing the subfolders
    folder_parentT = Path(path_project + "Dataset expected as output")
    # Use os.scandir to access the parent folder and retrieve only items that are folders:
    # .is_dir().
    # Obtain the list of subfolder paths:
    under_folders_pathT = [fT.path for fT in os.scandir(folder_parentT) if fT.is_dir()]
    # Obtain the list of subfolder names:
    under_folders_nameT = [fT_1.name for fT_1 in os.scandir(folder_parentT) if fT_1.is_dir()]
    # However, the path formatting is incorrect; it needs to be adjusted:
    under_folders_pathT = [Path(dT) for dT in under_folders_pathT]
    # Iterate through the books in under_folders_pathT
    for k in range(len(under_folders_pathT)):
        # For each folder:
        # Create its key in dictest_1 and the associated sub-dictionary.
        # Get the name of the sub-folder
        nameT = under_folders_nameT[k]
        # Check that it is not in L_name_books_errors
        if nameT not in L_name_books_errors:
            # Indicate current processing:
            print(nameT)
            # Create its key:
            dictest_3[nameT] = []
            # Traverse it. Retrieve all files in the folder:
            # Get the folder path:
            folder_currentT = under_folders_pathT[k]
            # Retrieve all text files
            # Get a list of them:
            filesT = os.listdir(folder_currentT)
            # Sort this list in ascending order:
            # Remove the extension (i.e., the last 4 characters), since we only have .txt files.
            filesT = [f[:-4] for f in filesT]
            # Sort the list
            filesT = natsorted(filesT)
            # Create list l1 for the book:
            # Create l1, ranging from 0 to the size of the filesT list.
            # This list corresponds to the size of the "universe" (the set of files).
            # Specifically, the files from the annotated folder: filesT.
            l1 = list(range(len(filesT)))
            # And list l2:
            # For each index in l2 (corresponding to an annotated file),
            # we need either -10 (if the file does not exist) or its rank.
            l2 = [-10 for k in range(len(filesT))]
            # Traverse it:
            # Iterate through l1 and check if the file corresponding to that index exists.
            for k1 in range(len(filesT)): 
                fileT = filesT[k1]
                # For each file
                # Retrieve its content:
                # Get the file using .glob on the folder with its name: fileT
                fileT_1 = folder_currentT.glob(fileT+".txt")
                for fileT_2 in fileT_1:
                    with open(fileT_2, "r", encoding="utf-8") as fT_2:
                        contentT = fT_2.read()
                # Go to the associated folder within the non-annotated folder. 
                # Create the path:
                path_non_annotatedT = Path(path_project+"folder_exit4/"+nameT)
                # Retrieve all file names without extensions. 
                # Then sort them (ignoring extensions) 
                # to iterate through them in ascending order. 
                # Later, recreate them with their extensions 
                # to access their contents. 
                files_non_annotatedT = path_non_annotatedT.glob("*.txt")
                # Extract only the names (without extensions) so they can be sorted numerically: 
                files_non_annotatedT = [name_avec_extT.stem for name_avec_extT in files_non_annotatedT]
                # Sort this list in ascending order:
                files_non_annotatedT = natsorted(files_non_annotatedT)
                # Initialize step b to 0:
                b = 0
                # Check if it can be found in the non-annotated folder
                for file_non_annotatedT in files_non_annotatedT:
                    # We recreate the file reference later with its extension
                    # in order to access its content.
                    # We check if the content matches one of the files.
                    # We retrieve the content of the annotated file:
                    # We locate the file using .glob on the folder with its name: fileT
                    file_non_annotatedT_1 = path_non_annotatedT.glob(file_non_annotatedT + ".txt")
                    for file_non_annotatedT_2 in file_non_annotatedT_1:
                        with open(file_non_annotatedT_2, "r", encoding="utf-8") as fT_3:
                            contentT_1 = fT_3.read()
                    # We check if this is the file we are looking for.
                    # We iterate through l1 and check if this file matches the annotated file at the current index.
                    if contentT == contentT_1:
                        # If so, we assign b to l2.
                        l2[k1] = b
                        # And we break the loop here.
                        break
                    # We increment b if the condition was not met, meaning we must continue iterating through the files.
                    b += 1
                    # If, ultimately, the file is not found among the annotated files, it was a false positive;
                    # therefore, removing it was the right decision.
            # We add the two lists to the dictionaries for this book.
            dictest_3[nameT] = [l1,l2]
    
    return dictest_3


# We will implement the generalized Kendall principle as defined by Emond & Mason.
# The generalized Kendall principle allows for the comparison of ranked lists.
# Specifically, the Emond & Mason approach handles cases with ties within the lists or lists of unequal lengths.
# This method is generally applied to descending lists—e.g., l = [a, b, c] where a > b > c.
# We will be using it with descending lists.

# We calculate the Kendall correlation for each book.
# We call the function: fKendall(dictest_3)
def fKendall(dictest_3):
    # Iterate through dictest_3
    keys = dictest_3.keys()
    # List of tau values:
    L_taus = []
    # Iterate through the books
    for key in keys:
        print(key)
        # For each book, retrieve l1 and l2
        l1 = dictest_3[key][0]
        l2 = dictest_3[key][1]
        #print(l1)
        #print(l2)
        # Create the universe—i.e., the list of all possible elements found in both lists (effectively l1).
        univers = l1
        # Create the two matrixs
        # Two lists of lists
        # For each list: populate it with a sub-list for k in range(len(univers)). And in each sub-list, set the value to 0 for k in range(len(univers)).
        # The advantage of using lists here is that the matrix indices correspond to the values ​​in our universe.
        matrix1 = [[0 for k in range(len(univers))]for k in range(len(univers))]
        matrix2 = [[0 for k in range(len(univers))]for k in range(len(univers))]
        # Iterate through each matrix and populate it with the correct values.
        # For matrix1
        # Iterate through each row—i.e., each list within matrix1—using index k1.
        for k1 in range(len(matrix1)):
            # For each row, store the value corresponding to that row's index in value_line.
            value_line = l1[k1]
            # Then iterate through the row's indices using index k2 (the row being matrix1[k1]).
            for k2 in range(len(matrix1[k1])):
                # For each index, retrieve the corresponding value from l1.
                value_colonne = l1[k2]
                # If k1 == k2: Set matrix1[k1][k2] to 0, as we are on the diagonal.
                if k1 == k2:
                    matrix1[k1][k2] = 0
                else:
                    # Note: We are following the generalized Kendall principle (Emond & Mason), but with the > and < conditions inverted,
                    # because we are dealing with a descending list.
                    # If this value is greater than or equal to our current value, set matrix1[k1][k2] to 1.
                    if value_colonne >= value_line:
                        matrix1[k1][k2] = 1
                    # If this value is strictly less than our current value. We put -1 in matrix1[k1][k2].
                    if value_colonne < value_line:
                        matrix1[k1][k2] = -1

        # For matrix2
        # Iterate through each row (i.e., each list within matrix2) using index k1_1.
        for k1_1 in range(len(matrix2)):
            # For each row, retrieve the value associated with that row's index from l2.
            value_line_1 = l2[k1_1]
            # If the value is -10, it means there is no initial data for this index;
            # therefore, we must set all elements in this row to 0:
            # For the row:
            if value_line_1 == -10:
                matrix2[k1_1] = [0 for k in range(len(matrix2[k1_1]))]
            else:
                # Otherwise, iterate through the indices of the row (matrix2[k1_1]) using k2_1.
                for k2_1 in range(len(matrix2[k1_1])):
                    # For each index, look up the corresponding value in l2.
                    value_colonne_1 = l2[k2_1]
                    # If k1_1 == k2_1, set matrix2[k1_1][k2_1] to 0, as we are on the diagonal.
                    if k1_1 == k2_1:
                        matrix2[k1_1][k2_1] = 0
                    else:
                        # If the value is -10, it means there is no initial data for this index;
                        # therefore, we must set all elements in this row and column to 0:
                        # For the column:
                        if value_colonne_1 == -10:
                            matrix2[k1_1][k2_1] = 0
                        else:
                            # Recall: we follow the generalized Kendall principle (Emond & Mason), but with the > and < conditions reversed.
                            # This is because we are dealing with a descending list.
                            # If this value is greater than or equal to our value, set matrix2[k1_1][k2_1] to 1.
                            if value_colonne_1 >= value_line_1:
                                matrix2[k1_1][k2_1] = 1
                            # If this value is strictly less than our value, set matrix2[k1_1][k2_1] to -1.
                            if value_colonne_1 < value_line_1:
                                matrix2[k1_1][k2_1] = -1

        # Calculate the total score.
        # Calculate tau:
        # The numerator:
        # Total sum:
        S = 0
        # P: the number of concordant pairs.
        P = 0
        # Q: the number of non-concordant pairs.
        Q = 0
        # S = P - Q
        # Iterate through the pairs:
        # The goal is to iterate through all possible pairs in the universe.
        # Two pairs are concordant if they have the same value in matrix1
        # as in matrix2
        # And for each of these pairs, add 1 to P if the pair is concordant
        # And for each of these pairs, add 1 to Q if the pair is non-concordant
        # Iterate through all indices to get all pairs
        for k in range(len(univers)-1): 
            for i in range(k+1,len(univers)):
                # We have matrix1,k,i
                value1 = matrix1[k][i]
                # We have matrix2,k,i
                value2 = matrix2[k][i]
                if value1 != 0 and value2 != 0:
                    #print("both different from 0")
                    if value1 == value2:
                        P += 1 
                    if ((value1 == 1) and (value2 == -1)) or ((value1 == -1) and (value2 == 1)):
                        Q += 1

        # We have that S = P - Q
        S = P - Q

        # THE denominator: As the denominator, we take len(univers)*(len(univers) - 1)/2
        denominator = len(univers)*(len(univers) - 1)/2
        # Tau
        tau = S/denominator
        L_taus.append(tau)
    
    return L_taus


# We call the function: fcreationl.
dictest_3 = fcreationl()
# And if, conversely, we are missing some files:
# We will have a list that is shorter than the other.

# Test
#list_score_kendall = fKendall(dictest_3)
#print("The list of Kendall scores is:")
#print(list_score_kendall)

# We calculate the Kendall correlation across all books:
# We will provide the average, as it makes no sense to calculate it for the entire set of books.
def score_kendall_total(list_score_kendall):
    # Number of scores:
    n = len(list_score_kendall)
    # Total sum of scores:
    S = 0
    for k in range(n):
        S += list_score_kendall[k]
    # We calculate the average
    moyenne_score_kendall = S/n
    return moyenne_score_kendall


""" RESULTS """
# The dictionaries:
dictest1 = fT1()
dictest2 = fT2()
dictest_3 = fcreationl()
# The results
L_recalls, L_accuracys, L_fscores, recall_total, accuracy_total, f_score_total = fmetrics(dictest1,dictest2)
list_score_kendall = fKendall(dictest_3)
tau_kendall_moyen = score_kendall_total(list_score_kendall)

# We create graphical representations in the form of histograms:
# For the recalls 
plt.bar(list(range(len(L_recalls))),L_recalls)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("book numbers")
plt.ylabel("recalls")
plt.title("book recalls")
plt.show()
plt.hist(L_recalls)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("recalls")
plt.ylabel("Number of books")
plt.title("histogram of book recalls")
plt.show()
print("total recall is")
print(recall_total)
# For accuracies
plt.bar(list(range(len(L_accuracys))),L_accuracys)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("book numbers")
plt.ylabel("accuracies")
plt.title("book accuracies")
plt.show()
plt.hist(L_accuracys)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("accuracies")
plt.ylabel("Number of books")
plt.title("histogram of book accuracies")
plt.show()
print("total accuracy is")
print(accuracy_total)
# For f-scores
plt.bar(list(range(len(L_fscores))),L_fscores)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid()
plt.xlabel("book numbers")
plt.ylabel("f-scores")
plt.title("book f-scores")
plt.show()
plt.hist(L_fscores)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.grid()
plt.xlabel("f-scores")
plt.ylabel("Number of books")
plt.title("histogram of book f-scores")
plt.show()
print("total f-score is")
print(f_score_total)

# Kendall's tau
plt.bar(list(range(len(list_score_kendall))),list_score_kendall)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel("book numbers")
plt.ylabel("Kendall's tau")
plt.title("Kendall's tau for the books")
plt.show()
plt.hist(list_score_kendall)
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 1.05, 0.05))
plt.xlabel("Kendall's tau")
plt.ylabel("Number of books")
plt.title("Histogram of Kendall's tau for the books")
plt.show()
print("The average Kendall's tau/score (excluding false positives) is:")
print(tau_kendall_moyen)
