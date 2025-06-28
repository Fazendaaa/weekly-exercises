#                                   Introduction
#
# The Zebra Puzzle is a famous logic puzzle in which there are five houses, each
# painted a different color. The houses have different inhabitants, who have
# different nationalities, own different pets, drink different beverages and
# enjoy different hobbies.
#
# To help you solve the puzzle, you're given 15 statements describing the
# solution. However, only by combining the information in all statements will
# you be able to find the solution to the puzzle.
#
#   Note
#
# The Zebra Puzzle is a Constraint satisfaction problem (CSP). In such a
# problem, you have a set of possible values and a set of constraints that limit
# which values are valid. Another well-known CSP is Sudoku.
#
#   Instructions
#
# Your task is to solve the Zebra Puzzle to find the answer to these two
# questions:
#
# - Which of the residents drinks water?
# - Who owns the zebra?
#
#   Puzzle
#
# The following 15 statements are all known to be true:
#
#   - There are five houses.
#   - The Englishman lives in the red house.
#   - The Spaniard owns the dog.
#   - The person in the green house drinks coffee.
#   - The Ukrainian drinks tea.
#   - The green house is immediately to the right of the ivory house.
#   - The snail owner likes to go dancing.
#   - The person in the yellow house is a painter.
#   - The person in the middle house drinks milk.
#   - The Norwegian lives in the first house.
#   - The person who enjoys reading lives in the house next to the person with
#     the fox.
#   - The painter's house is next to the house with the horse.
#   - The person who plays football drinks orange juice.
#   - The Japanese person plays chess.
#   - The Norwegian lives next to the blue house.
#
# Additionally, each of the five houses is painted a different color, and their
# inhabitants are of different national extractions, own different pets, drink
# different beverages and engage in different hobbies.
#
# Note
#
# There are 24 billion (5!⁵ = 24,883,200,000) possible solutions, so try ruling
# out as many solutions as possible.
#
# References:
#   - https://exercism.org/tracks/r/exercises/zebra-puzzle
#   - https://en.wikipedia.org/wiki/Zebra_Puzzle
#


from typing import Any


class Zebra:
    """A class to solve the Zebra Puzzle logic problem.

    The Zebra Puzzle involves 5 houses with different colors, inhabitants of different
    nationalities, pets, beverages and hobbies. The puzzle provides 15 clues that must be
    used together to determine who drinks water and who owns the zebra.

    Attributes:
        __houses__ (range): Range of house numbers from 1-5
        __colors__ (set): Set of house colors
        __nationalities__ (set): Set of inhabitant nationalities
        __animals__ (set): Set of pets owned by inhabitants
        __drinks__ (set): Set of beverages consumed by inhabitants
        __cigars__ (set): Set of cigar brands smoked by inhabitants
        __pets__ (set): Set of pets owned by inhabitants

    Properties:
        houses: Get/set the house numbers
        colors: Get/set the house colors
        nationalities: Get/set the inhabitant nationalities
        animals: Get/set the pets
        drinks: Get/set the beverages
        cigars: Get/set the cigar brands
    """

    def __init__(
        self,
        houses: int | None = None,
        colors: set[str] | None = None,
        nationalities: set[str] | None = None,
        animals: set[str] | None = None,
        drinks: set[str] | None = None,
        cigars: set[str] | None = None,
        pets: set[str] | None = None,
    ) -> None:
        self.__houses__: dict[int, Any] = {}
        self.__colors__: set[str] = set()
        self.__nationalities__: set[str] = set()
        self.__animals__: set[str] = set()
        self.__drinks__: set[str] = set()
        self.__cigars__: set[str] = set()
        self.__pets__: set[str] = set()

    def solve(self) -> None:
        """_summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("This method is not implemented yet.")

    def result(self) -> None:
        """_summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("This method is not implemented yet.")

    @property
    def houses(self) -> dict[int, Any]:
        """_summary_

        Returns:
            set[str]: _description_
        """
        return self.__houses__

    @property.setter
    def houses(self, houses: int) -> None:
        self.__houses__ = {i: None for i in range(1, houses + 1)}

    @property
    def colors(self) -> set[str]:
        return self.__colors__

    @property.setter
    def colors(self, colors: set[str]) -> None:
        self.__colors__ = colors

    @property
    def nationalities(self) -> set[str]:
        return self.__nationalities__

    @property.setter
    def nationalities(self, nationalities: set[str]) -> None:
        self.__nationalities__ = nationalities

    @property
    def animals(self) -> set[str]:
        return self.__animals__

    @property.setter
    def animals(self, animals: set[str]) -> None:
        self.__animals__ = animals

    @property
    def drinks(self) -> set[str]:
        return self.__drinks__

    @property.setter
    def drinks(self, drinks: set[str]) -> None:
        self.__drinks__ = drinks

    @property
    def cigars(self) -> set[str]:
        return self.__cigars__

    @property.setter
    def cigars(self, cigars: set[str]) -> None:
        self.__cigars__ = cigars

    @property
    def pets(self) -> set[str]:
        return self.__pets__

    @property.setter
    def pets(self, pets: set[str]) -> None:
        self.__pets__ = pets
