# EPUB Chapter Extraction & Classification Pipeline

This project is a Python pipeline that takes a folder of `.epub` files and, for each book, extracts its internal files (from the table of contents), filters out corrupted or badly-structured books, and classifies each remaining file as a **chapter**, **prologue**, **epilogue**, or **non-chapter content** (copyright page, glossary, acknowledgements, publisher page, about-the-author, etc.).

It was built to process a large, heterogeneous dataset of EPUB books (EPUB 2 and EPUB 3) and produce a clean, labeled dataset of "chapter" vs. "non-chapter" text files, suitable for downstream NLP tasks.

The objective was the minimisation of the false negatives.

## How it works — pipeline overview

The pipeline runs in numbered stages, each reading the output of the previous one and writing to a new `folder_exitX` directory inside the project folder. Two parallel "tracks" exist:

- **Track A (TOC-based, `.ncx` / `nav.xhtml`)** — for the ~88% of books with a usable, well-formed table of contents. This is the main track (`total.py`).
- **Track B (OPF-based fallback, `.opf` spine)** — for books that were rejected by Track A because their TOC entries didn't match a clean numeric sequence. Track B re-processes those same books using the reading order declared in the `.opf` manifest/spine instead of the TOC (`total2.py`, invoked from within `total.py`).

### Stage 1 — Data extraction (`extraction_of_the_datas.py`)
Opens every `.epub` in the input folder, locates the `.ncx` (EPUB 2) or `nav.xhtml` (EPUB 3) table of contents, and:
- Extracts every internal content file listed in the TOC, in reading order, saving each one as a numbered file (`1`, `2`, `3`, ...) in `folder_exit1/<book_name>/`.
- Builds `dic1` — for each book, the list of `[entry_title, filename]` pairs taken from the TOC.
- Builds `dic2` — for each book, a dictionary mapping play order → `[total_files, filename, play_order]`.
- Collects `list_bad_books` — EPUBs that fail to open or parse (non-compliant with the EPUB 2/3 standard).
- Returns `L_name_books_withoutext` — the list of book names (folder names, without extension) that were successfully processed.

### Stage 2 — HTML → plain text conversion (`transformation_in_texts.py`)
Uses **Calibre**'s `ebook-convert` command-line tool (via `subprocess`) to convert every extracted HTML/XHTML file into a plain `.txt` file, preserving the folder structure (`folder_exit1` → `folder_exit2`).

### Stage 2.1 — Duplicate/near-empty file detection (`detect_errors2.py`)
For each book, checks whether consecutive files are identical *and* nearly empty (fewer than 20 tokens) — a sign of a poorly structured EPUB. If detected, the whole book is discarded (moved to `list_bad_books`, removed from the dictionaries). Otherwise, the book folder is transferred as-is to `folder_exit3`.

### Stage 3 — TOC-based chapter/prologue/epilogue detection (`detector_of_references.py`)
Builds `dic3`: for every file of every book, decides whether it is likely a **chapter/prologue/epilogue** (`1`), an excluded section such as copyright/epigraph/glossary/about-the-author/about-the-publisher/also-by (`-1`), or undetermined (`0`). Detection combines:
- Keyword matching (case-insensitive) on the TOC entry title and on the filename.
- A numeric-sequence detector (`f2détec3`) that looks for consecutive integers (`1, 2, 3, ...`) appearing as TOC titles/filenames, a strong signal of a chapter sequence.

### Stage 3.1 — Content-based validation of "chapter" files (`detect_errors3.py`)
For every file flagged `1` in `dic3`, verifies the actual text content isn't near-empty (< 20 tokens). If any such file fails, the whole book is discarded. Books that pass are transferred to `folder_exit3_1`.

### Stage 5 — OPF-based fallback for rejected books (`total2.py`, using `extraction_of_the_datas5.py` and `detector_of_references5.py`)
Re-attempts extraction and the next stages before 3.1 for the books discarded earlier (in `list_bad_books`) using the EPUB's `.opf` spine order instead of the TOC (files only have a filename, no title text, so classification here relies on filename keywords plus the numeric-sequence check). Results are merged back into `dic1`, `dic2`, `dic3` and `L_name_books_withoutext`.

### Stage 4 — Fine-grained content-based classification (`detector_chap.py`)
For every file still marked "undetermined" (`0`) in `dic3`, runs a battery of content heuristics to catch non-chapter material that keyword/sequence matching missed:
- **Acknowledgements** — stemmed-word density of thank/grateful/gratitude roots.
- **Titles/short sections** — fewer than 200 tokens.
- **Copyright pages** — short text containing "copyright" and/or the © symbol.
- **Glossaries** — presence of the word "glossary", a high density of `:` characters, or long runs of lines whose first letters are in alphabetical order (a strong glossary/index signature).
- **Publisher pages** — stemmed "publish" root plus URL/imprint-like tokens (`www`, `.Inc`, `.Ltd`, `https`).

Files that end up flagged as chapters (`0` or `1`) are copied into `folder_exit4/<book_name>/`, the final, cleaned dataset of chapter files.

### Orchestration (`total.py`)
Runs the whole pipeline end-to-end (Stage 1 → 2.1 → 3 → 3.1 → 5 → 4) and prints final statistics: total number of files processed, how many were classified as chapters (`1`), non-chapters (`-1`), undetermined (`0`), and how many books were kept vs. discarded.

### Evaluation (`Test.py`)
A standalone evaluation script that compares the pipeline's output (`folder_exit4`) against a manually annotated ground-truth dataset. It computes, per book and overall:
- **Recall** and **accuracy** (precision) of chapter detection, plus the derived **F-score**.
- **Kendall's tau** rank-correlation, to measure how well the detected reading order matches the true chapter order. The Kendall's tau is the one following the generalized Kendall principle as defined by Emond & Mason. And we do not take into account the false positives.
It also plots bar charts and histograms of these metrics using `matplotlib`.

## Configuration (`criterias.py`)

All paths and detection keywords are centralized here so nothing is hard-coded elsewhere:
- `path_project` — root folder of the project (**edit this to your local path**, forward slashes only).
- `path_calibre` — path to the Calibre `ebook-convert` executable.
- Keyword criteria: `c_chapter`, `c_prologue`, `c_epilogue`, `c_copyright`, `c_epigraph`, `c_glossary`, `c_about_author`, `c_about_publisher`, `c_also_by`.
- `language` — language used for stemming (`SnowballStemmer`), currently `"english"`.
- `L_roots_acknowledgements`, `L_words_publisher`, `c_publisher` — word lists/roots used by the acknowledgements and publisher detectors.
- `c_Copyright`, `logo_Copyright` — copyright-page markers.

## Requirements

- Python 3
- [Calibre](https://calibre-ebook.com/) installed locally (for `ebook-convert`, used in the HTML→text conversion step)
- Python packages:
  - `ebooklib`
  - `beautifulsoup4` (with an `xml` parser backend, e.g. `lxml`)
  - `nltk` (with the `punkt_tab` tokenizer data — downloaded automatically at runtime)
  - `natsort`
  - `matplotlib`, `numpy` (for `Test.py` only)

Install with:
```bash
pip install ebooklib beautifulsoup4 lxml nltk natsort matplotlib numpy
```
- The epubs that you put in the program must respect the norm Epub 2 or the norm Epub 3. In fact, most of the epubs that you can find are respecting these rules. If your book/folder does not it means that it is not an epub.

## Setup

1. Edit `criterias.py` and set `path_project` to your project's root folder, and `path_calibre` to your local Calibre installation.
2. Place your `.epub` files in a subfolder named `epubs` inside `path_project`.
3. Run the full pipeline:
```bash
python total.py
```
4. (Optional) Once you have a manually annotated ground-truth folder (`Dataset expected as output`), run the evaluation script:
```bash
python Test.py
```

## Output folders

All intermediate and final folders are created automatically inside `path_project`:

| Folder | Content |
|---|---|
| `folder_exit1` | Raw extracted HTML/XHTML files, one subfolder per book (TOC-based track) |
| `folder_exit2` | Same files converted to plain text |
| `folder_exit3` | Books that passed the duplicate/near-empty check |
| `folder_exit3_1` | Books that passed the content validation of chapter files |
| `folder_exit5_1` / `folder_exit5_2` | Equivalent stages for the OPF-based fallback track (Stage 5) |
| `folder_exit4` | **Final output**: cleaned files classified as chapters, one subfolder per book |

## Notes / known limitations

- The pipeline currently assumes chapter/section numbering uses Arabic numerals. But you can easily modify the code if you need. 
- Re-running the pipeline on the same input is safe: output folders aren't recreated if they already exist, and files are simply overwritten — but this adds unnecessary computation. The stage: Stage 2 — HTML → plain text conversion (`transformation_in_texts.py`) is the reason that the program can takes multiple hours. If all your files have already been transformed you can bypass this by commenting this stage in total.py. It is easy. Eventually the running time is divided by a huge factor, a factor of 50 for instance.
- Also, if the program fails or if you stop it during stage 2, suppress the folder: folder_temporary if it appears before re-running, otherwise it will make the program fail.
- In the program now are two examples of epubs, found legally on gutenberg. One where we can use the .ncx and one where we have to use the .opf, to show you the different possibilites of the program.

## Results

With 40 random books, from many sources with 2081 files:
- 0% of the books discarded because malformed. 100% of the books kept and analyzed.
- On the 2081 files of the 40 books. 18.6% of books annotated as non chapters, 69.8% annotated as chapters. And 11.6% non annotated, considered as chapters. 

## Metrics

With 40 random books, from many sources with 2081 files:
The objective was the minimisation of the false negatives, so the maximisation of the recall, wich is detrimental to the accuracy.
- The total **recall** is : 0.99
- The total **accuracy** is : 0.96
- The total **f-score** is : 0.97
- The **Kendall score** : 0.98