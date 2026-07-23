print("Step 1 starting")
# Handling step 1.
# Import the file
import extraction_of_the_datas
# Apply function f1 from extraction_of_the_datas to the 'epubs' folder
# Retrieve the two dictionaries.
# test
dic1, dic2, list_bad_books, L_name_books_withoutext = extraction_of_the_datas.f1("epubs")
print("Step 1 completed")


"""
print("Step 2 starting")
# Handling step 2.
# transformation_in_texts.py 
# Create the function 'transformation_total' (based on part 1).
# It takes an input folder and an output folder as variables: folder_entry_total, folder_exit_total
# These are the folder names, not their full paths.

# Run the function with "folder_exit1" as input and "folder_exit2" as output
import transformation_in_texts
transformation_in_texts.transformation_total("folder_exit1","folder_exit2")
print("Step 2 completed")
"""


print("Step 2.1 starting") 
# Handling step 2.1:
# detect_bet.py
# f21(folder_exit2,folder_exit3,dic1, dic2, list_bad_books, L_name_books_withoutext)
import detect_errors2
dic1, dic2, list_bad_books, L_name_books_withoutext = detect_errors2.f21("folder_exit2","folder_exit3",dic1, dic2, list_bad_books, L_name_books_withoutext)
print("Step 2.1 completed")


print("Step 3 starting")
# We'll handle step 3.
# Step 3 takes dictionary 1 and L_name_books_withoutext as input and outputs dictionary 3.
import detector_of_references
dic3 = detector_of_references.fabrication_dictionnary3(dic1,L_name_books_withoutext)
print("Step 3 completed")


print("Step 3.1 starting") 
# We'll handle step 3.1
# Step 3.1 takes the following as input: "folder_exit3", "folder_exit3_1", dic1, dic2, dic3, list_bad_books, L_name_books_withoutext.
# And outputs: dic1, dic2, dic3, list_bad_books, L_name_books_withoutext.
import detect_errors3
dic1, dic2, dic3, list_bad_books, L_name_books_withoutext = detect_errors3.f31("folder_exit3","folder_exit3_1",dic1, dic2, dic3, list_bad_books, L_name_books_withoutext)
print("Step 3.1 completed")

print(list_bad_books)
print(L_name_books_withoutext)

print("Step 5 starting")
# We'll handle step 5.
# Import the code file
import total2 
dic1,dic2,dic3,list_bad_books,L_name_books_withoutext = total2.ftotal2(dic1,dic2,dic3,list_bad_books,L_name_books_withoutext, "epubs","folder_exit3_1")
print("Step 5 completed")


print("Step 4 starting")
# We'll handle step 4.
# fprincipal5(dict2,dict3,L_name_books_withoutext):
# It returns nothing; it only modifies files. #Import the code file
import detector_chap
dic3_final = detector_chap.fprincipal5(dic2,dic3,L_name_books_withoutext)
print("Step 4 completed")

print("dictionnary of the books, their files and the annotation of each file and the list of the bad books")
print(dic3_final,list_bad_books)


# We want to retrieve:
# The keys of dic3_final
keys = dic3_final.keys() 
# The count of these sub-keys in dic3_final
nb_under_keys = 0
nb_under_keys0 = 0
nb_under_keys1 = 0
nb_under_keysmoins1 = 0
# We iterate through the keys of dic3_final:
for key in keys:
    # We iterate through the sub-keys:
    under_keys = dic3_final[key].keys()
    for under_key in under_keys:
        # For each one:
        value = dic3_final[key][under_key]
        # The number of sub-keys in dic3_final equal to 0
        if value == 0:
            nb_under_keys0 += 1
        # The number of sub-keys in dic3_final equal to 1
        if value == 1:
            nb_under_keys1 += 1
        # The number of sub-keys in dic3_final equal to -1
        if value == -1:
            nb_under_keysmoins1 += 1
        # +1 to the count of these sub-keys in dic3_final
        nb_under_keys += 1

print("nb_under_keys: total number of files")
print(nb_under_keys)
print("nb_under_keys0: total number of files neither detected as Chapters nor Non chapters")
print(nb_under_keys0)
print("nb_under_keys1: total number of files detected as Chapters")
print(nb_under_keys1)
print("nb_under_keysmoins1: total number of files detected as Non chapters")
print(nb_under_keysmoins1)
print("number of bad books, that have been discarded")
print(len(list_bad_books))
print("number of good books, that have not been discarded")
print(len(L_name_books_withoutext))


