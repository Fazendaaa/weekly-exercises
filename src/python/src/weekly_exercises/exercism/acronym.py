#                               Instructions
#
# Convert a phrase to its acronym.
#
# Techies love their TLA (Three Letter Acronyms)!
#
# Help generate some jargon by writing a program that converts a long name like
# Portable Network Graphics to its acronym (PNG).
#
# Punctuation is handled as follows: hyphens are word separators (like
# whitespace); all other punctuation can be removed from the input.
#
# For example:
#
#   Input	                    Output
#   As Soon As Possible	        ASAP
#   Liquid-crystal display	    LCD
#   Thank George It's Friday!	TGIF
#
# Reference:
#   -https://exercism.org/tracks/python/exercises/acronym
#

from re import IGNORECASE, sub


def abbreviate(value: str) -> str:
    """
    Convert a phrase to its acronym by taking the first letter of each word.

    Args:
        value (str): The input phrase to convert to an acronym

    Returns:
        str: The acronym created from the first letter of each word, in uppercase

    Examples:
        >>> abbreviate("As Soon As Possible")
        'ASAP'
        >>> abbreviate("Liquid-crystal display")
        'LCD'
        >>> abbreviate("Thank George It's Friday!")
        'TGIF'

    Notes:
        - Hyphens are treated as word separators (like spaces)
        - Commas and underscores are removed from input
        - Only words starting with letters are included in acronym
        - All punctuation except hyphens is ignored
    """
    empty = sub(r",|_", "", value, flags=IGNORECASE)
    clean = sub(r"-", " ", empty, flags=IGNORECASE)

    return "".join(
        [
            item[0].upper()
            for item in clean.split(" ")
            if len(item) and item[0].isalpha()
        ]
    )
