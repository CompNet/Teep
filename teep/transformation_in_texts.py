import subprocess
import os
import shutil
import tempfile
from pathlib import Path


def convert_html_to_txt(input_file: Path, output_file: Path, ebook_convert_path: str):
    try:
        subprocess.run([ebook_convert_path, str(input_file), str(output_file)])
        print(f"Conversion successful")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


def epub_to_text(input_dir: Path, output_dir: Path, ebook_convert_path: str):
    book_folders = [f for f in input_dir.iterdir() if f.is_dir()]

    for book_folder in book_folders:
        book_output_dir = output_dir / book_folder.name
        book_output_dir.mkdir(parents=True, exist_ok=True)

        for input_file in book_folder.glob("*"):
            output_file = (book_output_dir / input_file.name).with_suffix(".txt")
            convert_html_to_txt(input_file, output_file, ebook_convert_path)
