import argparse
from pathlib import Path
from teep.data_extraction import extract_html
from teep.transformation_in_texts import epub_to_text
from teep.detect_errors2 import detect_erroneous_epubs
from teep.detector_of_references import build_dic3
from teep.detect_errors3 import detect_file_type
from teep.detector_chap import filter_chapter
from teep.total2 import opf_fallback
from teep.config import TeepConfig


def extraction_pipeline(input_dir: Path):

    config = TeepConfig(root_path=input_dir.parent)

    print("Step 1 starting")
    dic1, dic2, list_bad_books, L_name_books_withoutext = extract_html(
        input_dir, input_dir.parent / "folder_exit1"
    )
    print("Step 1 completed")

    print("Step 2 starting")
    epub_to_text(
        input_dir.parent / "folder_exit1",
        input_dir.parent / "folder_exit2",
        config.ebook_convert_path,
    )
    print("Step 2 completed")

    print("Step 2.1 starting")
    dic1, dic2, list_bad_books, L_name_books_withoutext = detect_erroneous_epubs(
        input_dir.parent / "folder_exit2",
        input_dir.parent / "folder_exit3",
        dic1,
        dic2,
        list_bad_books,
        L_name_books_withoutext,
    )
    print("Step 2.1 completed")

    print("Step 3 starting")
    dic3 = build_dic3(dic1, L_name_books_withoutext, config)
    print("Step 3 completed")

    print("Step 3.1 starting")
    dic1, dic2, dic3, list_bad_books, L_name_books_withoutext = detect_file_type(
        input_dir.parent / "folder_exit3",
        input_dir.parent / "folder_exit3_1",
        dic1,
        dic2,
        dic3,
        list_bad_books,
        L_name_books_withoutext,
    )
    print("Step 3.1 completed")

    print(list_bad_books)
    print(L_name_books_withoutext)

    print("Step 5 starting")
    dic1, dic2, dic3, list_bad_books, L_name_books_withoutext = opf_fallback(
        input_dir,
        input_dir.parent / "folder_exit3_1",
        dic1,
        dic2,
        dic3,
        list_bad_books,
        L_name_books_withoutext,
        config.ebook_convert_path,
        config,
    )
    print("Step 5 completed")

    print("Step 4 starting")

    # We'll handle step 4.
    # It returns nothing; it only modifies files.
    dic3_final = filter_chapter(
        input_dir.parent / "folder_exit3_1",
        input_dir.parent / "folder_exit4",
        dic3,
        config,
    )
    print("Step 4 completed")

    print(
        "dictionnary of the books, their files and the annotation of each file and the list of the bad books"
    )
    print(dic3_final, list_bad_books)

    # We want to retrieve:
    # The count of these sub-keys in dic3_final
    nb_under_keys = 0
    nb_under_keys0 = 0
    nb_under_keys1 = 0
    nb_under_keysmoins1 = 0
    # We iterate through the keys of dic3_final:
    for key in dic3_final.keys():
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
    print(
        "nb_under_keys0: total number of files neither detected as Chapters nor Non chapters"
    )
    print(nb_under_keys0)
    print("nb_under_keys1: total number of files detected as Chapters")
    print(nb_under_keys1)
    print("nb_under_keysmoins1: total number of files detected as Non chapters")
    print(nb_under_keysmoins1)
    print("number of bad books, that have been discarded")
    print(len(list_bad_books))
    print("number of good books, that have not been discarded")
    print(len(L_name_books_withoutext))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", type=Path, help="epub input directory")
    args = parser.parse_args()

    extraction_pipeline(args.input_dir)


if __name__ == "__main__":
    main()
