#                                   Pig Latin
#
#   Introduction
#
# Your parents have challenged you and your sibling to a game of two-on-two
# basketball. Confident they'll win, they let you score the first couple of
# points, but then start taking over the game. Needing a little boost, you start
# speaking in Pig Latin, which is a made-up children's language that's difficult
# for non-children to understand. This will give you the edge to prevail over
# your parents!
#
#   Instructions
#
# Your task is to translate text from English to Pig Latin. The translation is
# defined using four rules, which look at the pattern of vowels and consonants
# at the beginning of a word. These rules look at each word's use of vowels and
# consonants:
#
#   - vowels: the letters a, e, i, o, and u
#   - consonants: the other 21 letters of the English alphabet
#
#   Rule 1
#
# If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound
# to the end of the word.
#
# For example:
#   - "apple" -> "appleay" (starts with vowel)
#   - "xray" -> "xrayay" (starts with "xr")
#   - "yttria" -> "yttriaay" (starts with "yt")
#
#   Rule 2
#
# If a word begins with one or more consonants, first move those consonants to
# the end of the word and then add an "ay" sound to the end of the word.
#
# For example:
#   - "pig" -> "igp" -> "igpay" (starts with single consonant)
#   - "chair" -> "airch" -> "airchay" (starts with multiple consonants)
#   - "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
#
#   Rule 3
#
# If a word starts with zero or more consonants followed by "qu", first move
# those consonants (if any) and the "qu" part to the end of the word, and then
# add an "ay" sound to the end of the word.
#
# For example:
#   - "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding
#     consonants)
#   - "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by
#     "qu")
#
#   Rule 4
#
# If a word starts with one or more consonants followed by "y", first move the
# consonants preceding the "y"to the end of the word, and then add an "ay" sound
# to the end of the word.
#
# Some examples:
#   - "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
#   - "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants
#     followed by "y")
#
# Reference:
# - https://exercism.org/tracks/python/exercises/pig-latin
#

from re import findall


class PigLatin:
    """A class to translate English text to Pig Latin.

    Pig Latin is a language game that follows specific rules for transforming English words.
    The translation depends on the pattern of vowels and consonants at the beginning of each word.

    Attributes:
        __sentence__ (str): The input sentence to be translated, converted to lowercase
        __vowels__ (str): String containing all vowels (a,e,i,o,u)
        __consonants__ (str): String containing all consonants
    """

    def __init__(
        self,
        sentence: str,
    ) -> None:
        """Initialize PigLatin translator with input sentence.

        Args:
            sentence (str): The English text to be translated to Pig Latin
        """
        self.__sentence__ = sentence.lower()
        self.__vowels__ = "aeiou"
        self.__consonants__ = "bcdfghjklmnpqrstvwxyz"

    def __startsWith__(
        self,
        group: str,
        word: str,
    ) -> bool:
        """Check if word starts with any character from the given group.

        Args:
            group (str): String of characters to check against
            word (str): Word to check

        Returns:
            bool: True if word starts with any character from group, False otherwise
        """
        return [] != findall(rf"\b[{group}]\w*", word)

    def __translate_word__(
        self,
        word: str,
    ) -> str:
        """Translate a single word to Pig Latin.

        Applies the rules of Pig Latin translation:
        1. Words beginning with vowels or 'xr'/'yt' add 'ay' to the end
        2. Words beginning with consonants move those consonants to end and add 'ay'
        3. Words with 'qu' move everything up to and including 'qu' to end and add 'ay'
        4. Words with consonants followed by 'y' move consonants to end and add 'ay'

        Args:
            word (str): Single word to translate

        Returns:
            str: Word translated to Pig Latin
        """
        if (
            self.__startsWith__(self.__vowels__, word)
            or word.startswith("xr")
            or word.startswith("yt")
        ):
            return word + "ay"

        if self.__startsWith__(self.__consonants__, word):
            if word.startswith("qu"):
                return word[2:] + "quay"

            if "y" == word[1]:
                return word[1:] + word[0] + "ay"

            for index, value in enumerate(word):
                if value in self.__vowels__:
                    return word[index:] + word[:index] + "ay"

                if "y" == value:
                    return word[index:] + word[:index] + "ay"

        return word

    def translate(self) -> str:
        """Translate the full sentence to Pig Latin.

        Splits sentence into words, translates each word, and recombines with proper capitalization.

        Returns:
            str: Complete sentence translated to Pig Latin with first letter capitalized
        """
        return " ".join(
            [self.__translate_word__(word) for word in self.__sentence__.split()]
        ).capitalize()
