#                               Complex Numbers
#
#   Instructions
#
# A complex number is expressed in the form z = a + b * i, where:
#
#   - a is the real part (a real number),
#   - b is the imaginary part (also a real number), and
#   - i is the imaginary unit satisfying i^2 = -1.
#
#   Operations on Complex Numbers
#
#   Conjugate
#
# The conjugate of the complex number z = a + b * i is given by:
#
#   zc = a - b * i
#
#   Absolute Value
#
# The absolute value (or modulus) of z is defined as:
#
#   |z| = sqrt(a^2 + b^2)
#
# The square of the absolute value is computed as the product of z and its
# conjugate zc:
#
# |z|^2 = z * zc = a^2 + b^2
#
#   Addition
#
# The sum of two complex numbers z1 = a + b * i and z2 = c + d * i is computed
# by adding their real and imaginary parts separately:
#
# z1 + z2 = (a + b * i) + (c + d * i)
#         = (a + c) + (b + d) * i
#
#   Subtraction
#
# The difference of two complex numbers is obtained by subtracting their
# respective parts:
#
# z1 - z2 = (a + b * i) - (c + d * i)
#         = (a - c) + (b - d) * i
#
#   Multiplication
#
# The product of two complex numbers is defined as:
#
# z1 * z2 = (a + b * i) * (c + d * i)
#         = (a * c - b * d) + (b * c + a * d) * i
#
#   Reciprocal
#
# The reciprocal of a non-zero complex number is given by:
#
# 1 / z = 1 / (a + b * i)
#       = a / (a^2 + b^2) - b / (a^2 + b^2) * i
#
#   Division
#
# The division of one complex number by another is given by:
#
# z1 / z2 = z1 * (1 / z2)
#         = (a + b * i) / (c + d * i)
#         = (a * c + b * d) / (c^2 + d^2) + (b * c - a * d) / (c^2 + d^2) * i
#
#   Exponentiation
#
# Raising e (the base of the natural logarithm) to a complex exponent can be
# expressed using Euler's formula:
#
# e^(a + b * i) = e^a * e^(b * i)
#               = e^a * (cos(b) + i * sin(b))
#
#   Implementation Requirements
#
# Given that you should not use built-in support for complex numbers, implement
# the following operations:
#
#   - addition of two complex numbers
#   - subtraction of two complex numbers
#   - multiplication of two complex numbers
#   - division of two complex numbers
#   - conjugate of a complex number
#   - absolute value of a complex number
#   - exponentiation of e (the base of the natural logarithm) to a complex number
#
#   Building a Numeric Type
#
# See Emulating numeric types for help on operator overloading and customization.
#
# Reference
#   -https://en.wikipedia.org/wiki/Complex_number
#   -https://exercism.org/tracks/python/exercises/complex-numbers
#

from math import cos, e, sin, sqrt
from typing import Any


class Complex:

    def __init__(self, real: int | float, imaginary: int | float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: "Complex | Any") -> bool:
        if isinstance(other, Complex):
            return self.real == other.real and self.imaginary == other.imaginary

        raise ValueError(
            f"Operation equals not defined for Complex and { type(other) }"
        )

    def __repr__(self) -> str:
        return f"Complex(real={self.real}, imaginary={self.imaginary})"

    def __add__(self, other: "Complex | Any") -> "Complex":
        if isinstance(other, Complex):
            return Complex(
                self.real + other.real,
                self.imaginary + other.imaginary,
            )

        if isinstance(other, (int, float)):
            return Complex(
                self.real + other,
                self.imaginary,
            )

        raise ValueError(f"Operation add not defined for Complex and { type(other) }")

    def __radd__(self, other: Any) -> "Complex":
        if isinstance(other, (int, float)):
            return Complex(
                self.real + other,
                self.imaginary,
            )

        raise ValueError(f"Operation add not defined for Complex and { type(other) }")

    def __sub__(self, other: "Complex | Any") -> "Complex":
        if isinstance(other, Complex):
            return Complex(
                self.real - other.real,
                self.imaginary - other.imaginary,
            )

        if isinstance(other, (int, float)):
            return Complex(
                self.real - other,
                self.imaginary,
            )

        raise ValueError(
            f"Operation subtraction not defined for Complex and { type(other) }"
        )

    def __rsub__(self, other: Any) -> "Complex":
        if isinstance(other, (int, float)):
            return Complex(
                other - self.real,
                -self.imaginary,
            )

        raise ValueError(
            f"Operation subtraction not defined for Complex and { type(other) }"
        )

    def __mul__(self, other: "Complex | Any") -> "Complex":
        if isinstance(other, Complex):
            return Complex(
                (self.real * other.real) - (self.imaginary * other.imaginary),
                (self.real * other.imaginary) + (self.imaginary * other.real),
            )

        if isinstance(other, (int, float)):
            return Complex(
                self.real * other,
                self.imaginary * other,
            )

        raise ValueError(
            f"Operation multiplication not defined for Complex and { type(other) }"
        )

    def __rmul__(self, other: Any) -> "Complex":
        if isinstance(other, (int, float)):
            return Complex(
                self.real * other,
                self.imaginary * other,
            )

        raise ValueError(
            f"Operation multiplication not defined for Complex and { type(other) }"
        )

    def __truediv__(self, other: "Complex | Any") -> "Complex":
        if isinstance(other, Complex):
            real = (self.real * other.real) + (self.imaginary * other.imaginary)
            imaginary = (self.imaginary * other.real) - (self.real * other.imaginary)
            denominator = other.real**2 + other.imaginary**2

            return Complex(
                real / denominator,
                imaginary / denominator,
            )

        if isinstance(other, (int, float)):
            return Complex(
                self.real / other,
                self.imaginary / other,
            )

        raise ValueError(
            f"Operation division not defined for Complex and { type(other) }"
        )

    def __rtruediv__(self, other: Any) -> "Complex":
        if isinstance(other, (int, float)):
            denominator = self.real**2 + self.imaginary**2

            return Complex(
                other * self.real / denominator,
                -other * self.imaginary / denominator,
            )

        raise ValueError(
            f"Operation division not defined for Complex and { type(other) }"
        )

    def __abs__(self) -> int | float:
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self) -> "Complex":
        return Complex(self.real, -self.imaginary)

    def exp(self) -> "Complex":
        base = e**self.real

        return Complex(
            base * cos(self.imaginary),
            base * sin(self.imaginary),
        )
