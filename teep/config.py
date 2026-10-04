from typing import Literal
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TeepConfig:
    root_path: Path
    ebook_convert_path: str = "ebook-convert"

    # Chapter type minuscule criteria:
    c_chapter: str = "chapter"
    # Prologue type minuscule criteria:
    c_prologue: str = "prologue"
    # Epilogue type minuscule criteria:
    c_epilogue: str = "epilogue"
    # Other criterias:
    c_copyright: str = "copyright"
    # Copyright Criteria:
    c_Copyright: str = "Copyright"
    logo_Copyright: str = "©"
    # Root for publisher: According to STEM:
    c_publisher: str = "publish"
    c_epigraph: str = "epigraph"
    c_glossary: str = "glossary"
    c_about_author: str = "about the author"
    c_about_publisher: str = "aubout the publisher"
    c_also_by: str = "also by"

    # the language used for STEM racinisation:
    # notably, possibilities
    """arabic danish dutch english finnish french german hungarian italian norwegian porter portuguese romanian russian spanish swedish"""
    language: Literal[
        "arabic",
        "danish",
        "dutch",
        "english",
        "finnish",
        "french",
        "german",
        "hungarian",
        "italian",
        "norwegian",
        "porter",
        "portuguese",
        "romanian",
        "russian",
        "spanish",
        "swedish",
    ] = "english"

    # List of roots for acknowledgments: According to STEM:
    # In English:
    L_roots_acknowledgements: list[str] = field(
        default_factory=lambda: ["thank", "grate", "gratitud"]
    )

    # List of criteria for: about the publisher
    # In English:
    L_words_publisher: list[str] = field(
        default_factory=lambda: ["www", ".Ltd", ".Inc", "https"]
    )
