from pytest import raises
from weekly_exercises.variableLengthQuantity import VariableLengthQuantity


def test_zero() -> None:
    assert VariableLengthQuantity.encode([0x0]) == [0x0]


def test_arbitrary_single_byte() -> None:
    assert VariableLengthQuantity.encode([0x40]) == [0x40]


def test_largest_single_byte() -> None:
    assert VariableLengthQuantity.encode([0x7F]) == [0x7F]


def test_smallest_double_byte() -> None:
    assert VariableLengthQuantity.encode([0x80]) == [0x81, 0x0]


def test_arbitrary_double_byte() -> None:
    assert VariableLengthQuantity.encode([0x2000]) == [0xC0, 0x0]


def test_largest_double_byte() -> None:
    assert VariableLengthQuantity.encode([0x3FFF]) == [0xFF, 0x7F]


def test_smallest_triple_byte() -> None:
    assert VariableLengthQuantity.encode([0x4000]) == [0x81, 0x80, 0x0]


def test_arbitrary_triple_byte() -> None:
    assert VariableLengthQuantity.encode([0x100000]) == [0xC0, 0x80, 0x0]


def test_largest_triple_byte() -> None:
    assert VariableLengthQuantity.encode([0x1FFFFF]) == [0xFF, 0xFF, 0x7F]


def test_smallest_quadruple_byte() -> None:
    assert VariableLengthQuantity.encode([0x200000]) == [0x81, 0x80, 0x80, 0x0]


def test_arbitrary_quadruple_byte() -> None:
    assert VariableLengthQuantity.encode([0x8000000]) == [0xC0, 0x80, 0x80, 0x0]


def test_largest_quadruple_byte() -> None:
    assert VariableLengthQuantity.encode([0xFFFFFFF]) == [0xFF, 0xFF, 0xFF, 0x7F]


def test_smallest_quintuple_byte() -> None:
    assert VariableLengthQuantity.encode([0x10000000]) == [0x81, 0x80, 0x80, 0x80, 0x0]


def test_arbitrary_quintuple_byte() -> None:
    assert VariableLengthQuantity.encode([0xFF000000]) == [0x8F, 0xF8, 0x80, 0x80, 0x0]


def test_maximum_32_bit_integer_input() -> None:
    assert VariableLengthQuantity.encode([0xFFFFFFFF]) == [0x8F, 0xFF, 0xFF, 0xFF, 0x7F]


def test_two_single_byte_values() -> None:
    assert VariableLengthQuantity.encode([0x40, 0x7F]) == [0x40, 0x7F]


def test_two_multi_byte_values() -> None:
    assert VariableLengthQuantity.encode([0x4000, 0x123456]) == [
        0x81,
        0x80,
        0x0,
        0xC8,
        0xE8,
        0x56,
    ]


def test_many_multi_byte_values() -> None:
    assert VariableLengthQuantity.encode(
        [0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000]
    ) == [
        0xC0,
        0x0,
        0xC8,
        0xE8,
        0x56,
        0xFF,
        0xFF,
        0xFF,
        0x7F,
        0x0,
        0xFF,
        0x7F,
        0x81,
        0x80,
        0x0,
    ]


def test_one_byte() -> None:
    assert VariableLengthQuantity.decode([0x7F]) == [0x7F]


def test_two_bytes() -> None:
    assert VariableLengthQuantity.decode([0xC0, 0x0]) == [0x2000]


def test_three_bytes() -> None:
    assert VariableLengthQuantity.decode([0xFF, 0xFF, 0x7F]) == [0x1FFFFF]


def test_four_bytes() -> None:
    assert VariableLengthQuantity.decode([0x81, 0x80, 0x80, 0x0]) == [0x200000]


def test_maximum_32_bit_integer() -> None:
    assert VariableLengthQuantity.decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]) == [0xFFFFFFFF]


def test_incomplete_sequence_causes_error() -> None:
    with raises(ValueError, match="incomplete sequence"):
        VariableLengthQuantity.decode([0xFF])


def test_incomplete_sequence_causes_error_even_if_value_is_zero() -> None:
    with raises(ValueError, match="incomplete sequence"):
        VariableLengthQuantity.decode([0xFF])


def test_multiple_values() -> None:
    assert VariableLengthQuantity.decode(
        [
            0xC0,
            0x0,
            0xC8,
            0xE8,
            0x56,
            0xFF,
            0xFF,
            0xFF,
            0x7F,
            0x0,
            0xFF,
            0x7F,
            0x81,
            0x80,
            0x0,
        ]
    ) == [0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000]
