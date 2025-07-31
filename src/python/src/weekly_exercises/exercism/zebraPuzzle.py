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

from typing import Any, Optional


class Zebra:
    """A class to solve the Zebra Puzzle logic problem with self-generated deductions."""

    def __init__(
        self,
        houses: Optional[int] = None,
        colors: Optional[set[str]] = None,
        nationalities: Optional[set[str]] = None,
        pets: Optional[set[str]] = None,
        drinks: Optional[set[str]] = None,
        hobbies: Optional[set[str]] = None,
    ) -> None:
        self.__houses__: dict[int, dict[str, Any]] = {}
        self.__colors__: set[str] = colors or set()
        self.__nationalities__: set[str] = nationalities or set()
        self.__pets__: set[str] = pets or set()
        self.__drinks__: set[str] = drinks or set()
        self.__hobbies__: set[str] = hobbies or set()
        self.__constraints__: list[dict] = []
        self.__attributes__ = ["color", "nationality", "pet", "drink", "hobby"]
        self.__position_attribute__ = "position"

        if houses is not None:
            self.houses = houses

    def relate(
        self, attribute1: str, value1: Any, relation: str, attribute2: str, value2: Any
    ) -> None:
        """Establishes a relationship between two attributes."""
        self.__constraints__.append(
            {
                "attribute1": attribute1,
                "value1": value1,
                "relation": relation,
                "attribute2": attribute2,
                "value2": value2,
            }
        )

    def solve(self) -> None:
        """Solves the puzzle using constraint satisfaction."""
        self._initialize_attributes()
        self._generate_all_possibilities()
        self._apply_constraints()
        self._eliminate_impossibilities()
        self._deduce_remaining_attributes()

    def _initialize_attributes(self) -> None:
        for house_num in self.houses:
            self.houses[house_num] = {
                "color": set(self.colors),
                "nationality": set(self.nationalities),
                "pet": set(self.pets),
                "drink": set(self.drinks),
                "hobby": set(self.hobbies),
                self.__position_attribute__: {house_num},
            }

    def _generate_all_possibilities(self) -> None:
        """Generate all possible combinations of attributes."""
        pass

    def _apply_constraints(self) -> None:
        """Apply all registered constraints to narrow possibilities."""
        for constraint in self.__constraints__:
            self._apply_constraint(constraint)

    def _apply_constraint(self, constraint: dict) -> None:
        """Apply a single constraint to the houses."""
        attr1 = constraint["attribute1"]
        val1 = constraint["value1"]
        relation = constraint["relation"]
        attr2 = constraint["attribute2"]
        val2 = constraint["value2"]

        if relation == "is":
            self._apply_is_relation(attr1, val1, attr2, val2)
        elif relation == "same_house":
            self._apply_same_house_relation(attr1, val1, attr2, val2)
        elif relation == "next_to":
            self._apply_next_to_relation(attr1, val1, attr2, val2)
        elif relation == "right_of":
            self._apply_right_of_relation(attr1, val1, attr2, val2)

    def _apply_is_relation(self, attr1: str, val1: Any, attr2: str, val2: Any) -> None:
        """Apply an 'is' relationship."""
        if attr1 == self.__position_attribute__:
            # Handle position constraints (e.g., "Norwegian is in position 1")
            for house_num, house in self.houses.items():
                if house_num == val1:
                    house[attr2] = {val2}
                elif val2 in house.get(attr2, set()):
                    house[attr2].remove(val2)
        else:
            # Handle other "is" constraints
            for house in self.houses.values():
                if val1 in house.get(attr1, set()):
                    if attr2 in house:
                        house[attr2] = {val2}
                    else:
                        house[attr2] = {val2}

    def _apply_same_house_relation(
        self, attr1: str, val1: Any, attr2: str, val2: Any
    ) -> None:
        """Apply same house relationship."""
        for house in self.houses.values():
            if val1 in house.get(attr1, set()):
                if attr2 in house:
                    if val2 not in house[attr2]:
                        house[attr2] = {val2}
                else:
                    house[attr2] = {val2}
            if val2 in house.get(attr2, set()):
                if attr1 in house:
                    if val1 not in house[attr1]:
                        house[attr1] = {val1}
                else:
                    house[attr1] = {val1}

    def _apply_next_to_relation(
        self, attr1: str, val1: Any, attr2: str, val2: Any
    ) -> None:
        """Apply next_to relationship."""
        for house_num, house in self.houses.items():
            if val1 in house.get(attr1, set()):
                # Find adjacent houses
                adjacent = []
                if house_num > 1:
                    adjacent.append(house_num - 1)
                if house_num < len(self.houses):
                    adjacent.append(house_num + 1)

                # Apply to adjacent houses
                for adj in adjacent:
                    if attr2 in self.houses[adj]:
                        if val2 in self.houses[adj][attr2]:
                            continue
                        else:
                            self.houses[adj][attr2] = {val2}
                    else:
                        self.houses[adj][attr2] = {val2}

    def _apply_right_of_relation(
        self, attr1: str, val1: Any, attr2: str, val2: Any
    ) -> None:
        """Apply right_of relationship (val1 is immediately right of val2)."""
        for i in range(1, len(self.houses)):
            # Check if house i+1 could have val1 and house i could have val2
            if val1 in self.houses[i + 1].get(attr1, set()):
                if attr2 in self.houses[i]:
                    if val2 not in self.houses[i][attr2]:
                        self.houses[i][attr2] = {val2}
                else:
                    self.houses[i][attr2] = {val2}

            if val2 in self.houses[i].get(attr2, set()):
                if attr1 in self.houses[i + 1]:
                    if val1 not in self.houses[i + 1][attr1]:
                        self.houses[i + 1][attr1] = {val1}
                else:
                    self.houses[i + 1][attr1] = {val1}

    def _eliminate_impossibilities(self) -> None:
        """Eliminate impossible values based on constraints."""
        changed = True
        while changed:
            changed = False
            changed |= self._propagate_constraints()
            changed |= self._eliminate_unique_values()

    def _propagate_constraints(self) -> bool:
        """Propagate constraints through the houses."""
        changed = False
        for house in self.houses.values():
            for attr in self.__attributes__:
                if attr in house and len(house[attr]) == 1:
                    # This attribute is determined, remove from other houses
                    value = next(iter(house[attr]))
                    for other_house in self.houses.values():
                        if (
                            other_house != house
                            and attr in other_house
                            and value in other_house[attr]
                        ):
                            other_house[attr].remove(value)
                            changed = True
        return changed

    def _eliminate_unique_values(self) -> bool:
        """If a value only appears once in an attribute across all houses, set it."""
        changed = False
        for attr in self.__attributes__:
            value_counts = {}
            for house in self.houses.values():
                if attr in house:
                    for value in house[attr]:
                        value_counts[value] = value_counts.get(value, 0) + 1

            for value, count in value_counts.items():
                if count == 1:
                    for house in self.houses.values():
                        if (
                            attr in house
                            and value in house[attr]
                            and len(house[attr]) > 1
                        ):
                            house[attr] = {value}
                            changed = True
        return changed

    def _deduce_remaining_attributes(self) -> None:
        """Deduce remaining attributes through logical elimination."""
        # Continue until all houses have all attributes determined
        while not all(
            all(len(v) == 1 for v in house.values()) for house in self.houses.values()
        ):
            self._propagate_constraints()
            self._eliminate_unique_values()

            # Additional deduction: if an attribute has only one possible house left
            for attr in self.__attributes__:
                possible_houses = []
                for house_num, house in self.houses.items():
                    if attr in house and len(house[attr]) > 1:
                        possible_houses.append(house_num)

                if len(possible_houses) == 1:
                    house_num = possible_houses[0]
                    for value in self.houses[house_num][attr]:
                        # Check if this value is possible in other houses
                        possible = True
                        for other_house_num, other_house in self.houses.items():
                            if (
                                other_house_num != house_num
                                and attr in other_house
                                and value in other_house[attr]
                            ):
                                possible = False
                                break
                        if possible:
                            self.houses[house_num][attr] = {value}
                            break

    @property
    def houses(self) -> dict[int, dict[str, Any]]:
        """Get the dictionary of houses and their attributes."""
        return self.__houses__

    @houses.setter
    def houses(self, num_houses: int) -> None:
        """Initialize the houses with the given number.

        Args:
            num_houses: Number of houses to initialize (should be 5 for the puzzle)
        """
        self.__houses__ = {i: {} for i in range(1, num_houses + 1)}

    @property
    def colors(self) -> set[str]:
        """Get the set of possible house colors."""
        return self.__colors__

    @colors.setter
    def colors(self, colors: set[str]) -> None:
        """set the possible house colors."""
        self.__colors__ = colors

    @property
    def nationalities(self) -> set[str]:
        """Get the set of possible nationalities."""
        return self.__nationalities__

    @nationalities.setter
    def nationalities(self, nationalities: set[str]) -> None:
        """set the possible nationalities."""
        self.__nationalities__ = nationalities

    @property
    def pets(self) -> set[str]:
        """Get the set of possible pets."""
        return self.__pets__

    @pets.setter
    def pets(self, pets: set[str]) -> None:
        """set the possible pets."""
        self.__pets__ = pets

    @property
    def drinks(self) -> set[str]:
        """Get the set of possible drinks."""
        return self.__drinks__

    @drinks.setter
    def drinks(self, drinks: set[str]) -> None:
        """set the possible drinks."""
        self.__drinks__ = drinks

    @property
    def hobbies(self) -> set[str]:
        """Get the set of possible hobbies."""
        return self.__hobbies__

    @hobbies.setter
    def hobbies(self, hobbies: set[str]) -> None:
        """set the possible hobbies."""
        self.__hobbies__ = hobbies
