#                               Matching Brackets
#
#   Introduction
#
# You're given the opportunity to write software for the Bracketeer™, an ancient
# but powerful mainframe. The software that runs on it is written in a
# proprietary language. Much of its syntax is familiar, but you notice lots of
# brackets, braces and parentheses. Despite the Bracketeer™ being powerful, it
# lacks flexibility. If the source code has any unbalanced brackets, braces or
# parentheses, the Bracketeer™ crashes and must be rebooted. To avoid such a
# scenario, you start writing code that can verify that brackets, braces, and
# parentheses are balanced before attempting to run it on the Bracketeer™.
#
#   Instructions
#
# Given a string containing brackets [], braces {}, parentheses (), or any
# combination thereof, verify that any and all pairs are matched and nested
# correctly. Any other characters should be ignored. For example,
# "{what is (42)}?" is balanced and "[text}" is not.
#
# Reference:
#
# https://exercism.org/tracks/python/exercises/matching-brackets
#

from typing import Literal

ENGINES = Literal[
    "stack",
    "recursive",
    "state",
]


class MatchingBrackets:
    """
    A class to verify that brackets, braces and parentheses are balanced in a string.

    Attributes:
        __sentence__ (str): The input string to check for balanced brackets.
    """

    def __init__(
        self,
        sentence: str,
    ) -> None:
        """
        Initialize a MatchingBrackets instance.

        Args:
            sentence (str): The string to check for balanced brackets.
        """
        self.__sentence__ = sentence

    def __repr__(self) -> str:
        """
        Return string representation of the MatchingBrackets instance.

        Returns:
            str: String representation showing the sentence being checked.
        """
        return f"MatchingBrackets({self.__sentence__})"

    def __stack__(self) -> bool:
        """
        Check for balanced brackets using a stack-based approach.

        Returns:
            bool: True if brackets are balanced, False otherwise.
        """
        stack: list[str] = []
        opening = "([{"
        closing = ")]}"
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in self.__sentence__:
            if char in opening:
                stack.append(char)

            if char in closing:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return not stack

    def __recursive__(self) -> bool:
        """
        Check for balanced brackets using a recursive approach.

        Returns:
            bool: True if brackets are balanced, False otherwise.
        """
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        def __recursive_helper__(
            sentence: str,
            last: str = "",
        ) -> bool:
            """
            Helper function for recursive bracket matching.

            Args:
                sentence (str): The string to check.

            Returns:
                bool: True if brackets are balanced, False otherwise.
            """
            if not sentence:
                return not last

            if sentence[0] in "([{":
                return __recursive_helper__(sentence[1:], sentence[0])

            if sentence[0] in ")]}":
                if not last or last != pairs[sentence[0]]:
                    return False
                return __recursive_helper__(sentence[1:], sentence[0])

            return __recursive_helper__(sentence[1:])

        return __recursive_helper__(self.__sentence__)

    def __state__(self) -> bool:
        """
        Check for balanced brackets using a state-based approach.

        Returns:
            bool: True if brackets are balanced, False otherwise.
        """
        lastState = 0
        actualState = 0
        PARENTHESIS = 1
        SQUARE_BRACKETS = 2
        CURLY_BRACES = 3

        for char in self.__sentence__:
            if "(" == char:
                actualState += PARENTHESIS
                lastState = PARENTHESIS
            if "[" == char:
                actualState += SQUARE_BRACKETS
                lastState = SQUARE_BRACKETS
            if "{" == char:
                actualState += CURLY_BRACES
                lastState = CURLY_BRACES

            if ")" == char:
                actualState -= PARENTHESIS

                if lastState and lastState != PARENTHESIS:
                    return False
                else:
                    lastState = 0
            if "]" == char:
                actualState -= SQUARE_BRACKETS

                if lastState and lastState != SQUARE_BRACKETS:
                    return False
                else:
                    lastState = 0
            if "}" == char:
                actualState -= CURLY_BRACES

                if lastState and lastState != CURLY_BRACES:
                    return False
                else:
                    lastState = 0

            if actualState < 0:
                return False

        return 0 == actualState

    def isPaired(
        self,
        engine: ENGINES = "stack",
    ) -> bool:
        """
        Check if brackets in the sentence are properly paired.

        Args:
            engine (ENGINES): The algorithm to use for checking brackets.
                            Options are "stack", "recursive", or "state".
                            Defaults to "stack".

        Returns:
            bool: True if brackets are properly paired, False otherwise.

        Raises:
            ValueError: If an invalid engine type is specified.
        """
        if "stack" == engine:
            return self.__stack__()
        if "recursive" == engine:
            return self.__recursive__()
        if "state" == engine:
            return self.__state__()

        raise ValueError("Invalid engine")
