import math

from weekly_exercises.complexNumbers import Complex


def test_real_part_of_a_purely_real_number() -> None:
    assert 1 == Complex(1, 0).real


def test_real_part_of_a_purely_imaginary_number() -> None:
    assert 0 == Complex(0, 1).real


def test_real_part_of_a_number_with_real_and_imaginary_part() -> None:
    assert 1 == Complex(1, 2).real


# Imaginary part


def test_imaginary_part_of_a_purely_real_number() -> None:
    assert 0 == Complex(1, 0).imaginary


def test_imaginary_part_of_a_purely_imaginary_number() -> None:
    assert 1 == Complex(0, 1).imaginary


def test_imaginary_part_of_a_number_with_real_and_imaginary_part() -> None:
    assert 2 == Complex(1, 2).imaginary


# Equality


def test_equality_first() -> None:
    assert Complex(1, 0) == Complex(1, 0)


def test_equality_second() -> None:
    assert Complex(1, 0) != Complex(2, 0)


# Arithmetic

# Addition


def test_add_purely_real_numbers() -> None:
    assert Complex(1, 0) + Complex(2, 0) == Complex(3, 0)


def test_add_purely_imaginary_numbers() -> None:
    assert Complex(0, 1) + Complex(0, 2) == Complex(0, 3)


def test_add_numbers_with_real_and_imaginary_part() -> None:
    assert Complex(1, 2) + Complex(3, 4) == Complex(4, 6)


# Subtraction


def test_subtract_purely_real_numbers() -> None:
    assert Complex(1, 0) - Complex(2, 0) == Complex(-1, 0)


def test_subtract_purely_imaginary_numbers() -> None:
    assert Complex(0, 1) - Complex(0, 2) == Complex(0, -1)


def test_subtract_numbers_with_real_and_imaginary_part() -> None:
    assert Complex(1, 2) - Complex(3, 4) == Complex(-2, -2)


# Multiplication


def test_imaginary_unit() -> None:
    assert Complex(0, 1) * Complex(0, 1) == Complex(-1, 0)


def test_multiply_purely_real_numbers() -> None:
    assert Complex(1, 0) * Complex(2, 0) == Complex(2, 0)


def test_multiply_purely_imaginary_numbers() -> None:
    assert Complex(0, 1) * Complex(0, 2) == Complex(-2, 0)


def test_multiply_numbers_with_real_and_imaginary_part() -> None:
    assert Complex(1, 2) * Complex(3, 4) == Complex(-5, 10)


# Division


def test_divide_purely_real_numbers() -> None:
    assert Complex(1, 0) / Complex(2, 0) == Complex(0.5, 0)


def test_divide_purely_imaginary_numbers() -> None:
    assert Complex(0, 1) / Complex(0, 2) == Complex(0.5, 0)


def test_divide_numbers_with_real_and_imaginary_part() -> None:
    assert Complex(1, 2) / Complex(3, 4) == Complex(0.44, 0.08)


# Absolute value


def test_absolute_value_of_a_positive_purely_real_number() -> None:
    assert abs(Complex(5, 0)) == 5


def test_absolute_value_of_a_negative_purely_real_number() -> None:
    assert abs(Complex(-5, 0)) == 5


def test_absolute_value_of_a_purely_imaginary_number_with_positive_imaginary_part() -> (
    None
):
    assert abs(Complex(0, 5)) == 5


def test_absolute_value_of_a_purely_imaginary_number_with_negative_imaginary_part() -> (
    None
):
    assert abs(Complex(0, -5)) == 5


def test_absolute_value_of_a_number_with_real_and_imaginary_part() -> None:
    assert abs(Complex(3, 4)) == 5


# Complex conjugate


def test_conjugate_a_purely_real_number() -> None:
    assert Complex(5, 0).conjugate() == Complex(5, 0)


def test_conjugate_a_purely_imaginary_number() -> None:
    assert Complex(0, 5).conjugate() == Complex(0, -5)


def test_conjugate_a_number_with_real_and_imaginary_part() -> None:
    assert Complex(1, 1).conjugate() == Complex(1, -1)


# Complex exponential function


def test_euler_s_identity_formula() -> None:
    assert Complex(0, math.pi).exp() == Complex(-1, 0)


def test_exponential_of_0() -> None:
    assert Complex(0, 0).exp() == Complex(1, 0)


def test_exponential_of_a_purely_real_number() -> None:
    assert Complex(1, 0).exp() == Complex(math.e, 0)


def test_exponential_of_a_number_with_real_and_imaginary_part() -> None:
    assert Complex(math.log(2) == math.pi).exp() == Complex(-2, 0)


def test_exponential_resulting_in_a_number_with_real_and_imaginary_part() -> None:
    assert Complex(math.log(2) / 2, math.pi / 4).exp() == Complex(1, 1)


# Operations between real numbers and complex numbers


def test_add_real_number_to_complex_number() -> None:
    assert Complex(1, 2) + 5 == Complex(6, 2)


def test_add_complex_number_to_real_number() -> None:
    assert 5 + Complex(1, 2) == Complex(6, 2)


def test_subtract_real_number_from_complex_number() -> None:
    assert Complex(5, 7) - 4 == Complex(1, 7)


def test_subtract_complex_number_from_real_number() -> None:
    assert 4 - Complex(5, 7) == Complex(-1, -7)


def test_multiply_complex_number_by_real_number() -> None:
    assert Complex(2, 5) * 5 == Complex(10, 25)


def test_multiply_real_number_by_complex_number() -> None:
    assert 5 * Complex(2, 5) == Complex(10, 25)


def test_divide_complex_number_by_real_number() -> None:
    assert Complex(10, 100) / 10 == Complex(1, 10)


def test_divide_real_number_by_complex_number() -> None:
    assert 5 / Complex(1, 1) == Complex(2.5, -2.5)


# Additional tests for this track


def test_equality_of_complex_numbers() -> None:
    assert Complex(1, 2) == Complex(1, 2)


def test_inequality_of_real_part() -> None:
    assert Complex(1, 2) != Complex(2, 2)


def test_inequality_of_imaginary_part() -> None:
    assert Complex(1, 2) != Complex(1, 1)
