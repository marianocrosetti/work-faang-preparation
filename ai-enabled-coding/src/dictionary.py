"""
Provides a good selection of words with get_prod_dictionary(),
or a toy dictionary with get_test_dictionary(), which might be
useful when you get started with Solver.
"""

from pathlib import Path
from typing import Set


def get_test_dictionary() -> Set[str]:
    """Returns a small test dictionary for development."""
    words = """
        abet abey able ably abut ache achy acid acne adze
        ajar akin alit alms aloe also alum amen amid amok
        anew ankh ante apex apse aqua arch area aria arms
        army arid ashy atom atop avow avid away axle axon
        easy hard
    """
    return set(words.split())


def get_prod_dictionary() -> Set[str]:
    """Returns the production dictionary from file."""
    return _read_file_dictionary("up_to_six_letters.txt")


def _read_file_dictionary(filename: str) -> Set[str]:
    """Reads dictionary from a file."""
    # Search paths for the dictionary file
    search_paths = [Path("data")]

    for search_path in search_paths:
        file_path = search_path / filename
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                return {word.strip() for word in f if word.strip()}

    # If not found in any search path, raise an error
    searched_paths = ", ".join(str(p) for p in search_paths)
    raise FileNotFoundError(
        f"Dictionary file '{filename}' not found in: {searched_paths}"
    )
