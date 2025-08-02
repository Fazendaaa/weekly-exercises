#                           Jumping Kangaroos
#
# Adapted from here, with less terrible instructions and a couple tweaks.
#
# Two kangaroos are jumping on a line. They start out at different points on the
# ine, and jump in the same direction at different speeds. Your task is to
# determine whether or not they'll ever land in the same spot at the same time
# (you'll just have to suspend disbelief for a moment and accept that two
# kangaroos, for the purpose of this kata, can occupy the same space at the same
# time :)
#
# Your function is given four arguments (kanga1, rate1, kanga2, rate2); the
# first kangaroo's starting point, the first kangaroo's speed, the second
# kangaroo's starting point, and the second kangaroo's speed.
#
# Return true if the above conditions are met, else false. Starting location and
# speed may vary wildly. The first kangaroo will usually start behind the second
# one and travel faster, but not always. Starting locations may be negative, but
# speeds will always be > 0.
#
# Example:
#
#   kangaroo(kanga1 = 0, speed1 = 3, kanga2 = 4, speed2 = 2)=> true //they meet on their fourth jump
#
# Other examples:
#
#   kangaroo(0,2,5,3)=> false //the first kangaroo starts behind, moves slower, and never catches up
#
# Brute force solutions are possible (and not discouraged), but you'll save
# yourself a lot of waiting time if you don't go that route :)
#
# Good luck!
#
# References:
#   - https://www.codewars.com/kata/5ae7e1522c5061beb7000051
#


from functools import reduce


class Competitor:
    def __init__(self, start: float, speed: float) -> None:
        self.__start__ = start
        self.__speed__ = speed
        self.__position__ = start

    def __repr__(self) -> str:
        return f"Competitor({self.__start__}, {self.__speed__})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Competitor):
            raise TypeError("Can only compare Competitor to Competitor")

        return self.__start__ == value.__start__ and self.__speed__ == value.__speed__


class Kangaroo(Competitor):
    def __repr__(self) -> str:
        return f"Kangaroo({self.__start__}, {self.__speed__})"


class Race:
    def __init__(self) -> None:
        self.__competitors__: list[Competitor] = []

    def addCompetitor(self, competitor: Competitor) -> None:
        self.__competitors__.append(competitor)

    def meet(self) -> bool:
        if len(self.__competitors__) < 2:
            raise Exception("Not enough competitors to meet.")

        groups = [
            [competitor.__speed__, competitor.__start__]
            for competitor in self.__competitors__
        ]
        speeds, starts = zip(*groups)

        if all(speeds[0] == speed for speed in speeds) and all(
            starts[0] == start for start in starts
        ):
            return True

        startsDiff = reduce(lambda accumulator, current: accumulator - current, starts)
        speedsDiff = reduce(
            lambda accumulator, current: accumulator - current, reversed(speeds)
        )

        return not startsDiff % speedsDiff and startsDiff * speedsDiff >= 0
