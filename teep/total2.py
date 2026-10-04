from pathlib import Path
from teep.extraction_of_the_datas5 import f1_5
from teep.transformation_in_texts import epub_to_text
from teep.detect_errors2 import detect_erroneous_epubs
from teep.detector_of_references5 import build_dic5
from teep.config import TeepConfig


def fmodificationlist(list_bad_books):
    # We want to keep only bad books inside. No extensions.
    # Before this, we need to remove either: "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "
    # Or: "This file does not comply with epub2 and epub3 standards: "
    # Every time.
    # Size of the first string to detect: n1. Index to be used as the last in the slicing.
    n1 = len(
        "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "
    )
    # Size of the second string to detect: n2. Index to be used as the last in the slicing.
    n2 = len("This file does not comply with the EPUB 2 and EPUB 3 standards: ")
    # Output list:
    list_bad_books_v2 = []
    for chain in list_bad_books:
        print(chain)
        if (
            chain[:n1]
            == "The book complies with EPUB 2 and 3 standards but was written in a haphazard manner: "
        ):
            list_bad_books_v2.append(chain[n1:])
        elif (
            chain[:n2]
            == "This file does not comply with the EPUB 2 and EPUB 3 standards: "
        ):
            list_bad_books_v2.append(chain[n2:])
        else:
            return "problem"
    return list_bad_books_v2


def opf_fallback(
    input_epub_dir: Path,
    output_dir: Path,
    dic1: dict,
    dic2: dict,
    dic3: dict,
    list_bad_books: list,
    L_name_books_withoutext: list,
    ebook_convert_path: str,
    config: TeepConfig,
) -> tuple[dict, dict, dict, list, list]:

    print(list_bad_books)

    print("Preprocessing begins")
    # Function to modify list_bad_books
    list_bad_books = fmodificationlist(list_bad_books)
    print("Preprocessing finished")

    print(list_bad_books)
    if len(list_bad_books) == 0:
        return dic1, dic2, dic3, list_bad_books, L_name_books_withoutext

    print("Step 1 begins")
    # Calling the new data retriever: extraction_of_the_datas5
    dic1_1, dic2_1, list_bad_books_1, L_name_books_withoutext_1 = f1_5(
        list_bad_books, input_epub_dir, input_epub_dir.parent / "folder_exit5_1"
    )
    print("Step 1 finished")

    print("Step 2 begins")
    # Step 2.
    epub_to_text(
        input_epub_dir.parent / "folder_exit5_1",
        input_epub_dir.parent / "folder_exit5_2",
        ebook_convert_path,
    )
    print("Step 2 finished")

    print("Step 2.1 begins")
    # We do 2.1
    dic1_1, dic2_1, list_bad_books_1, L_name_books_withoutext_1 = (
        detect_erroneous_epubs(
            input_epub_dir.parent / "folder_exit5_2",
            output_dir,
            dic1_1,
            dic2_1,
            list_bad_books_1,
            L_name_books_withoutext_1,
        )
    )
    print("Step 2.1 finished")

    print("Step 3 begins")
    # We name the new one 3. We name the new reference detector: detector_of_references5
    dic3_1 = build_dic5(dic1_1, L_name_books_withoutext_1, config)
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

    return dic1, dic2, dic3, list_bad_books, L_name_books_withoutext
