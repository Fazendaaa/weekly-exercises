#                               List Ops
#
# Instructions
#
# Implement basic list operations.
#
# In functional languages list operations like length, map, and reduce are very
# common. Implement a series of basic list operations, without using existing
# functions.
#
# The precise number and names of the operations to be implemented will be track
# dependent to avoid conflicts with existing names, but the general operations
# you will implement include:
#
#   - append (given two lists, add all items in the second list to the end of
#     the first list);
#   - concatenate (given a series of lists, combine all items in all lists into
#     one flattened list);
#   - filter (given a predicate and a list, return the list of all items for
#     which predicate(item) is True);
#   - length (given a list, return the total number of items within it);
#   - map (given a function and a list, return the list of the results of
#     applying function(item) on all items);
#   - foldl (given a function, a list, and initial accumulator, fold (reduce)
#     each item into the accumulator from the left);
#   - foldr (given a function, a list, and an initial accumulator, fold (reduce)
#     each item into the accumulator from the right);
#   - reverse (given a list, return a list with all the original items, but in
#     reversed order).
#
# Note, the ordering in which arguments are passed to the fold functions (foldl,
# foldr) is significant.
#
# Reference:
#   - https://exercism.org/tracks/python/exercises/list-ops
#


from functools import reduce
from typing import Any, Callable

from weekly_exercises.utils import flatten


class List:
    def __init__(self, items: list[Any] = []) -> None:
        self.__items__ = items
        self.__count__ = 0
        self.__length__()

    def __repr__(self) -> str:
        return f"List=({self.__items__})"

    def __eq__(self, other: "List | list[Any] | Any") -> bool:
        if isinstance(other, List):
            return self.get() == other.get()

        if isinstance(other, list):
            return self.get() == other

        raise ValueError(f"Operation equals not defined for List and { type(other) }")

    def __length__(self) -> None:
        self.__count__ = reduce(
            lambda accumulator, _: accumulator + 1, self.__items__, 0
        )

    def get(self) -> list[Any]:
        return self.__items__

    def append(self, values: list[Any]) -> "List":
        self.__items__ = self.__items__ + values
        self.__length__()

        return self

    def concat(self, values: list[list[Any]]) -> "List":
        return List(self.get() + flatten(values))

    def filter(self, function: Callable[[Any], bool]) -> "List":
        return List([item for item in self.get() if function(item)])

    def length(self) -> int:
        return self.__count__

    def map(self, function: Callable[[Any], Any]) -> "List":
        return List([function(item) for item in self.get()])

    def foldl[T](self, function: Callable[[Any, Any], Any], initial: T) -> T:
        return reduce(function, self.get(), initial)

    def foldr[T](self, function: Callable[[Any, Any], Any], initial: T) -> T:
        return reduce(
            lambda acc, item: function(item, acc), self.reverse().get(), initial
        )

    def reverse(self) -> "List":
        return List(
            [self.__items__[index] for index in range(self.length() - 1, -1, -1)]
        )
