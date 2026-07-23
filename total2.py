# Imports
# imports of code files:
import extraction_of_the_datas5
import transformation_in_texts
import detect_errors2
import detector_of_references5

 
def fmodificationlist(list_bad_books):
    # We want to keep only bad books inside. No extensions.
    # Before this, we need to remove either: "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "
    # Or: "This file does not comply with epub2 and epub3 standards: "
    # Every time.
    # Size of the first string to detect: n1. Index to be used as the last in the slicing.
    n1 = len("The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: ")
    # Size of the second string to detect: n2. Index to be used as the last in the slicing.
    n2 = len("This file does not comply with the EPUB 2 and EPUB 3 standards: ")
    # Output list:
    list_bad_books_v2 = []
    for chain in list_bad_books:
        print(chain)
        if chain[:n1] == "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: ":
            list_bad_books_v2.append(chain[n1:])
        elif chain[:n2] == "This file does not comply with the EPUB 2 and EPUB 3 standards: ":
            list_bad_books_v2.append(chain[n2:])
        else:
            return "problem"
    return list_bad_books_v2
 

# Global function to be called in total.py:
def ftotal2(dic1, dic2, dic3, list_bad_books, L_name_books_withoutext, folder_entry, folder_exit): 
    
    print(list_bad_books)

    print("Preprocessing begins")
    # Function to modify list_bad_books
    list_bad_books = fmodificationlist(list_bad_books)
    print("Preprocessing finished") 

    print(list_bad_books)

    print("Step 1 begins")
    # Calling the new data retriever: extraction_of_the_datas5
    dic1_1,dic2_1, list_bad_books_1, L_name_books_withoutext_1 = extraction_of_the_datas5.f1_5(list_bad_books,folder_entry)
    print("Step 1 finished")

    
    print("Step 2 begins")
    # Step 2.
    # Run the function with "folder_exit1" as input and "folder_exit2" as output within transformation_total.
    transformation_in_texts.transformation_total("folder_exit5_1","folder_exit5_2")
    print("Step 2 finished")
    

    print("Step 2.1 begins")
    # We do 2.1
    dic1_1, dic2_1, list_bad_books_1, L_name_books_withoutext_1 = detect_errors2.f21("folder_exit5_2",folder_exit,dic1_1, dic2_1, list_bad_books_1, L_name_books_withoutext_1)
    print("Step 2.1 finished")


    print("Step 3 begins")
    # We name the new one 3. We name the new reference detector: detector_of_references5
    dic3_1 = detector_of_references5.fabrication_dictionary5(dic1_1,L_name_books_withoutext_1)
    print("Step 3 finished")


    # Step 3.1:
    # We are skipping this step because it relies on step 3.1 (a TOC-based consistency check), whereas here we are basing the process on the .opf file instead of the TOC.
    # The .opf file contains only filenames, which can logically vary. 

    print("Posttreatment begins")
    # We merge the dictionaries and the lists.
    dic1 = dic1 | dic1_1
    dic2 = dic2 | dic2_1
    dic3 = dic3 | dic3_1
    list_bad_books = list_bad_books_1
    L_name_books_withoutext = L_name_books_withoutext + L_name_books_withoutext_1
    print("Posttreatment finished")

    return dic1,dic2,dic3,list_bad_books,L_name_books_withoutext
