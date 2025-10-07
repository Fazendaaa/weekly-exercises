#                                   Introduction
#
# Your friend Yaʻqūb works the counter at the busiest deli in town, slicing,
# weighing, and wrapping orders for a never-ending line of hungry customers. To
# keep things moving, each customer takes a numbered ticket when they arrive.
#
# When it’s time to call the next person, Yaʻqūb reads their number out loud,
# always in full English words to make sure everyone hears it clearly.
#
#   Instructions
#
# Given a number, your task is to express it in English words exactly as your
# friend should say it out loud. Yaʻqūb expects to use numbers from 0 up to
# 999,999,999,999.
#
# Examples:
#
# 0 → zero
# 1 → one
# 12 → twelve
# 123 → one hundred twenty-three
# 1,234 → one thousand two hundred thirty-four
#
#   Exception messages
#
# Sometimes it is necessary to raise an exception. When you do this, you should
# always include a meaningful error message to indicate what the source of the
# error is. This makes your code more readable and helps significantly with
# debugging. For situations where you know that the error source will be a
# certain type, you can choose to raise one of the built in error types, but
# should still include a meaningful message.
#
# This particular exercise requires that you use the raise statement to "throw"
# a ValueError if the number input to say() is out of range. The tests will only
# pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
# # if the number is negative
# raise ValueError("input out of range")
#
# # if the number is larger than 999,999,999,999
# raise ValueError("input out of range")
#
# References:
# - https://exercism.org/tracks/python/exercises/say
#


def say(value: int) -> str:
    """Convert a number to its English word representation.

    Takes an integer and returns a string containing the number expressed in English words.
    For example, 123 becomes "one hundred twenty-three".

    Args:
        value (int): The number to convert to words. Must be between 0 and 999,999,999,999.

    Returns:
        str: The English word representation of the number.

    Raises:
        ValueError: If value is negative or >= 1 trillion (10^12).

    Examples:
        >>> say(0)
        'zero'
        >>> say(123)
        'one hundred twenty-three'
        >>> say(1_234)
        'one thousand two hundred thirty-four'
    """
    if value < 0 or value >= 10**12:
        raise ValueError("input out of range")

    if value == 0:
        return "zero"

    ones = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if value < 1_000:
        result = ""

        if value >= 100:
            result += ones[value // 100] + " hundred"
            value %= 100

            if value > 0:
                result += " "
        if value >= 20:
            result += tens[value // 10]

            if value % 10 > 0:
                result += "-" + ones[value % 10]
        elif value >= 10:
            result += teens[value - 10]
        elif value > 0:
            result += ones[value]

        return result

    scales = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
    ]

    for scale_value, scale_name in scales:
        if value >= scale_value:
            before_scale = say(value // scale_value)
            after_scale = say(value % scale_value)

            result = before_scale + " " + scale_name

            if after_scale and "zero" != after_scale:
                result += " " + after_scale

            return result

    return ""
