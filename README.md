# Teep — Text Extraction from EPUBs

Teep is a Python pipeline that automatically extracts the textual content of EPUB files, cleans it up, and then isolates the actual chapters of a book by filtering out everything that isn't part of the narrative (acknowledgements, copyright, glossary, publisher pages, etc.).

The project aims to produce, for each book, a folder containing only the text files that correspond to chapters, prologues or epilogues.

## Table of contents

- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration (criterias.py)](#configuration-criteriaspy)
- [Pipeline structure](#pipeline-structure)
- [Usage](#usage)
- [Output folder structure](#output-folder-structure)
- [Internal dictionary structures](#internal-dictionary-structures)
- [Evaluation (Test.py)](#evaluation-testpy)
- [License](#license)
- [Results](#results)
- [Metrics](#metrics)
- [Results](#results)
- [Metrics](#metrics)

## How it works

To lauch the pipeline you have to put your epubs in the folder: epubs. And then run the file: total.py
You have to modify criterias.py with at least:
- the path of the project in your machine.
- the path to calibre in your machine. The path to: ebook-convert.exe.

And you can modify the rest of the criterias as you want.

The result will be in the folder: folder_exit4. A final folder containing, for each valid book, only the text files corresponding to actual chapters, epilogues and prologues. In the right order.

And the script total.py will also give:

- The dictionnary of annotations and the list of the book discarded with the reason. 
- A general overview of the annotations of the books.
- The number of books discarded and kept.

1. **Extraction** of the files of each book and extraction and creation of all the metadata. And first detection of malformed books. The books that are discarded are the books that do not respect the elementary rules of the norm Epub 2 or the norm Epub 3.
2. **Conversion** of these HTM/HTML/XHTML files into plain text via Calibre.
3. **First detection of malformed books** which are discarded from further processing.  The detection here is on the content of the files of the ebooks. We also discard the books where in the toc the references are to a the same file but to different part using the #. 
4. **First detection of Chapters and non Chapters** Based on the metadata (keywords, numeric sequences..). Based on the keywords that you can ajust in criterias.py.
5. **Second detection of malformed books** Based of the coherence between the metadatas and the real content of the ebook.
6. **Second detection of non Chapters** In the files still not detected as Chapters nor no Chapters. Based on the content of the ebooks. Using statistical heuristics and stemming. Based on the criterias in criterias.py that you can customize. Production of a final folder containing, for each valid book, only the text files corresponding to actual chapters, epilogues and prologues. In the right order.

## Requirements

- Python 3.x
- [Calibre](https://calibre-ebook.com/) installed (the script uses the `ebook-convert` executable bundled with Calibre)
- Python libraries:
  - `ebooklib`
  - `beautifulsoup4` (`bs4`)
  - `natsort`
  - `nltk` (with the `punkt_tab` resource)
  - `matplotlib`
  - `numpy`

## Installation

```bash
pip install ebooklib beautifulsoup4 natsort nltk matplotlib numpy
```

Make sure Calibre is installed on your machine and that the path to `ebook-convert` is correct (see configuration below).

## Configuration (`criterias.py`)

All the project's constants are centralized in `criterias.py`:

| Variable | Role |
|---|---|
| `path_project` | Absolute path to the project's root folder (containing the EPUBs and all intermediate folders). Must be adapted to your machine. |
| `path_calibre` | Path to Calibre's `ebook-convert` executable. |
| `c_chapter`, `c_prologue`, `c_epilogue` | Lowercase keywords used to spot chapters/prologues/epilogues. |
| `c_copyright`, `c_epigraph`, `c_glossary`, `c_about_author`, `c_about_publisher`, `c_also_by` | Keywords used to exclude sections that are not chapters. |
| `language` | Language used for NLTK stemming (Snowball Stemmer). Defaults to `"english"`. |
| `L_roots_acknowledgements` | Word roots used to detect acknowledgement pages. |
| `L_words_publisher`, `c_publisher` | Criteria used to detect publisher-related pages. |
| `c_Copyright`, `logo_Copyright` | Criteria used to detect copyright pages. |

**Before running anything, update `path_project` and `path_calibre` to match your environment.**

## Pipeline structure

`total.py` orchestrates the whole pipeline by calling the following modules in order:

| Step | Module | Function | Role |
|---|---|---|---|
| 1 | `extraction_of_the_datas.py` | `f1("epubs")` | Scans the EPUBs, extracts the table of contents (`.ncx`/`nav.xhtml`) and the corresponding files into `folder_exit1`. Builds `dic1` (TOC entry text + filename per book) and `dic2` (per-file metadata). |
| 2 | `transformation_in_texts.py` | `transformation_total("folder_exit1", "folder_exit2")` | Converts each extracted HTML/XHTML file into plain text via Calibre, into `folder_exit2`. |
| 2.1 | `detect_errors2.py` | `f21(...)` | Detects "malformed" books: at least 3 consecutive strictly identical files. These books are discarded; the others are moved to `folder_exit3`. |
| 3 | `detector_of_references.py` | `fabrication_dictionnary3(dic1, L_name_books_withoutext)` | Builds `dic3`: for each file of each book, flags whether it's a chapter (`1`), a section to exclude outright (`-1`, e.g. copyright/glossary/publisher), or neutral (`0`), based on the filename, the TOC entry text, and detection of numeric sequences in titles. |
| 3.1 | `detect_errors3.py` | `f31(...)` | For each file flagged as a chapter (`1`), checks that it contains at least 20 words. If a book contains a chapter that's too short, it is discarded; otherwise it's moved to `folder_exit3_1`. |
| 4 | `detector_chap.py` | `fprincipal5(dic2, dic3, L_name_books_withoutext)` | For files still marked "neutral" (`0`), applies 5 heuristic detectors (acknowledgements, section title, copyright, glossary, publisher) to flag them as `-1` if needed. Copies the remaining files (chapters, `0` or `1`) into `folder_exit4`, organized by book. |

At the end, `total.py` prints statistics: total number of classified files, breakdown by status (`0`, `1`, `-1`), number of discarded books (`list_bad_books`), and number of remaining valid books.

### Detail of the detectors in `detector_chap.py`

- `facknowledgements4`: ratio of (stemmed words matching "thank"/"gratitude") to (number of lines) ≥ 0.3.
- `ftitles4`: a file with fewer than 200 words is treated as a simple section title.
- `fcopyright4`: text shorter than 20 lines containing the word "copyright" and/or the "©" symbol.
- `fglossary4`: detects the word "glossary", a high density of ":" per line (> 70%), or a sequence of 13 consecutive lines whose first letters are alphabetically sorted (a typical signature of a glossary/index).
- `fpublisher4`: combines the "publish" root, textual clues (`www`, `.Inc`, `.Ltd`, `https`), and the presence of numbers, with a density threshold of 0.4 per line.

## Usage

1. Put your `.epub` files in an `epubs/` folder inside `path_project`.
2. Update `criterias.py` (paths).
3. Run:

```bash
python total.py
```

The script successively creates and populates `folder_exit1`, `folder_exit2`, `folder_exit3`, `folder_exit3_1`, and `folder_exit4` inside `path_project`, then prints a statistical summary to the console.
The script can be re-run multiple times on the same input folder without recreating already-existing folders (files are simply overwritten), at the cost of redundant computation.

## Output folder structure

| Folder | Content |
|---|---|
| `folder_exit1` | Raw HTML/XHTML files extracted from the EPUBs, one subfolder per book. |
| `folder_exit2` | Plain-text version of `folder_exit1` (after Calibre conversion). |
| `folder_exit3` | Books from `folder_exit2` that passed the anti-duplication filter. |
| `folder_exit3_1` | Books from `folder_exit3` whose detected chapters all contain at least 20 words. |
| `folder_exit4` | **Final output**: for each valid book, only the files corresponding to actual chapters. |

## Internal dictionary structures

- **`dic1`**: `{book_name: [[TOC_entry_text, filename], ...]}` — one entry per file referenced in the table of contents.
- **`dic2`**: `{book_name: {playorder: [total_nb_files, filename, playorder]}}` — per-file metadata.
- **`dic3`**: `{book_name: {playorder: status}}` where `status` is:
  - `1`: confirmed chapter
  - `0`: neutral / not yet decided
  - `-1`: to be excluded (acknowledgements, copyright, glossary, publisher page, epigraph, "also by", etc.)
- **`list_bad_books`**: list of messages describing books discarded from processing (not EPUB 2/3 compliant, duplicated, or containing chapters that are too short).
- **`L_name_books_withoutext`**: list of book names (without extension) still valid at a given stage of the pipeline.

## Evaluation (`Test.py`)

In the end you can also test the capacities of the program. With the code: Test.py.
You have lauched the pipeline and obtained the results in the folder: folder_exit4. And you want to evaluate these results.
You put the reference, the folders that you expect to obtain, folder containing a folder for each book, with in it only the text files corresponding to actual chapters, epilogues and prologues. In the right order. 
In the folder: Dataset expected as output.
In the list `L_name_books_errors` you the `list_bad_books` that you obtained when you launched total.py.
And you launch the program: Test.py.
You will obtain the metrics:

- **Recall**,**accuracy** and **F-score** per book and on average.
- **Kendall's tau** as defined by Emond & Mason to compare the order of detected chapters with the expected order. But the False positives are not taken into account.
- Generation of histograms and bar charts (via `matplotlib`) to visualize these metrics across all books.

## License

This project is distributed under the **GNU General Public License v3.0 (GPL-3.0)**. See the [`LICENSE`](./LICENSE) file for the full text.

## Results

With 40 random books, from many sources with 1342 files:
- 27.5% of the books discarded because malformed. 72.5% o the book kept and analyzed.
- On the 1342 files of the 40 books. 18.6% of books annotated as non chapters, 69.8% annotated as chapters. And 11.6% non annotated, considered as chapters. 

## Metrics

With 40 random books, from many sources with 1342 files:
- The total **recall** is : 0.9920755696007331
- The total **accuracy** is : 0.9809682181916577
- The total **f-score** is : 0.9862999512731967
- The **Kendall score** : 0.9640278444247414
