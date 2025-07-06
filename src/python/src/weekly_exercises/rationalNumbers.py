#                               Rational Numbers
#
#   Instructions
#
# A rational number is defined as the quotient of two integers a and b, called
# the numerator and denominator, respectively, where b != 0.
#
#   Note
#
# Note that mathematically, the denominator can't be zero. However in many
# implementations of rational numbers, you will find that the denominator is
# allowed to be zero with behaviour similar to positive or negative infinity in
# floating point numbers. In those cases, the denominator and numerator
# generally still can't both be zero at once.
#
# The absolute value |r| of the rational number r = a/b is equal to |a|/|b|.
#
# The sum of two rational numbers
# r₁ = a₁/b₁
# and
# r₂ = a₂/b₂
# is
# r₁ + r₂ = a₁/b₁ + a₂/b₂ = (a₁ * b₂ + a₂ * b₁) / (b₁ * b₂).
#
# The difference of two rational numbers
# r₁ = a₁/b₁
# and
# r₂ = a₂/b₂
# is
# r₁ - r₂ = a₁/b₁ - a₂/b₂ = (a₁ * b₂ - a₂ * b₁) / (b₁ * b₂).
#
# The product (multiplication) of two rational numbers
# r₁ = a₁/b₁
# and
# r₂ = a₂/b₂
# is
# r₁ * r₂ = (a₁ * a₂) / (b₁ * b₂).
#
# Dividing a rational number
# r₁ = a₁/b₁
# by another
# r₂ = a₂/b₂
# is
# r₁ / r₂ = (a₁ * b₂) / (a₂ * b₁)
# if
# a₂
# is not zero.
#
# Exponentiation of a rational number
# r = a/b
# to a non-negative integer power n is
# r^n = (a^n)/(b^n).
#
# Exponentiation of a rational number
# r = a/b
# to a negative integer power n is
# r^n = (b^m)/(a^m)
# , where m = |n|.
#
# Exponentiation of a rational number
# r = a/b
# to a real (floating-point) number x is the quotient
# (a^x)/(b^x)
# , which is a real number.
#
# Exponentiation of a real number x to a rational number
# r = a/b
# is
# x^(a/b) = root(x^a, b)
# , where
# root(p, q)
# is the qth root of p.
#
# Implement the following operations:
#
#   - addition, subtraction, multiplication and division of two rational
#     numbers,
#   - absolute value, exponentiation of a given rational number to an integer
#     power, exponentiation of a given rational number to a real
#     (floating-point) power, exponentiation of a real number to a rational
#     number.
#
# Your implementation of rational numbers should always be reduced to lowest
# terms. For example, 4/4 should reduce to 1/1, 30/60 should reduce to 1/2, 12/8
# should reduce to 3/2, etc. To reduce a rational number r = a/b, divide a and b
# by the greatest common divisor (gcd) of a and b. So, for example,
# gcd(12, 8) = 4, so r = 12/8 can be reduced to (12/4)/(8/4) = 3/2. The reduced
# form of a rational number should be in "standard form" (the denominator should
# always be a positive integer). If a denominator with a negative integer is
# present, multiply both numerator and denominator by -1 to ensure standard form
# is reached. For example, 3/-4 should be reduced to -3/4
#
# Assume that the programming language you are using does not have an
# implementation of rational numbers.
#
# Reference
#
#   - https://exercism.org/tracks/python/exercises/rational-numbers
#   - https://en.wikipedia.org/wiki/Rational_number
#

from math import gcd
from typing import Any


class Rational:

    def __init__(self, numerator: int | float, denominator: int | float) -> None:
        if not denominator:
            raise ValueError("Denominator cannot be zero")

        self.__numerator__ = int(numerator)
        self.__denominator__ = int(denominator)
        self.__summarize__()

    def __summarize__(self) -> None:
        if (self.__numerator__ < 0 and self.__denominator__ < 0) or (
            self.__denominator__ < 0 and self.__numerator__ > 0
        ):
            self.__numerator__ = -self.__numerator__
            self.__denominator__ = -self.__denominator__

        if result := gcd(self.__numerator__, self.__denominator__):
            self.__numerator__ = int(self.__numerator__ / result)
            self.__denominator__ = int(self.__denominator__ / result)

    def __eq__(self, other: "Rational | Any") -> bool:
        if isinstance(other, Rational):
            return (
                self.__numerator__ == other.__numerator__
                and self.__denominator__ == other.__denominator__
            )

        raise ValueError(
            f"Operation equals not defined for Rational and { type(other) }"
        )

    def __repr__(self) -> str:
        return f"Rational(numerator={self.__numerator__}, denominator={self.__denominator__})"

    def __add__(self, other: "Rational | Any") -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                self.__numerator__ * other.__denominator__
                + other.__numerator__ * self.__denominator__,
                self.__denominator__ * other.__denominator__,
            )

        raise ValueError(f"Operation add not defined for Rational and { type(other) }")

    def __sub__(self, other: "Rational | Any") -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                self.__numerator__ * other.__denominator__
                - other.__numerator__ * self.__denominator__,
                self.__denominator__ * other.__denominator__,
            )

        raise ValueError(
            f"Operation subtraction not defined for Rational and { type(other) }"
        )

    def __mul__(self, other: "Rational | Any") -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                self.__numerator__ * other.__numerator__,
                self.__denominator__ * other.__denominator__,
            )

        raise ValueError(
            f"Operation multiplication not defined for Rational and { type(other) }"
        )

    def __truediv__(self, other: "Rational | Any") -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                self.__numerator__ * other.__denominator__,
                self.__denominator__ * other.__numerator__,
            )

        raise ValueError(
            f"Operation division not defined for Rational and { type(other) }"
        )

    def __pow__(self, other: "Rational | Any") -> "Rational":
        if isinstance(other, int):
            if 0 > other:
                power = -other

                return Rational(
                    self.__denominator__**power,
                    self.__numerator__**power,
                )

            return Rational(
                self.__numerator__**other,
                self.__denominator__**other,
            )

        raise ValueError(f"Operation pow not defined for Rational and { type(other) }")

    def __abs__(self) -> "Rational":
        return Rational(
            self.__numerator__ if self.__numerator__ > 0 else -self.__numerator__,
            self.__denominator__ if self.__denominator__ > 0 else -self.__denominator__,
        )

    def __rpow__(self, other: int | float) -> float:
        return (other ** (1 / self.__denominator__)) ** self.__numerator__
