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
    clean = sub(r",|_|-", " ", value, flags=IGNORECASE)
    items = clean.split(" ")

    return "".join([item[0].upper() for item in items if item[0].isalpha()])
