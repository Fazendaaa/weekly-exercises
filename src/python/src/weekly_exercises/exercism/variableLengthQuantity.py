#                               Instructions
#
# Implement variable length quantity encoding and decoding.
#
# The goal of this exercise is to implement VLQ encoding/decoding.
#
# In short, the goal of this encoding is to encode integer values in a way that
# would save bytes. Only the first 7 bits of each byte are significant
# (right-justified; sort of like an ASCII byte). So, if you have a 32-bit value,
# you have to unpack it into a series of 7-bit bytes. Of course, you will have a
# variable number of bytes depending upon your integer. To indicate which is the
# last byte of the series, you leave bit #7 clear. In all of the preceding
# bytes, you set bit #7.
#
# So, if an integer is between 0-127, it can be represented as one byte.
# Although VLQ can deal with numbers of arbitrary sizes, for this exercise we
# will restrict ourselves to only numbers that fit in a 32-bit unsigned integer.
# Here are examples of integers as 32-bit values, and the variable length
# quantities that they translate to:
#
# NUMBER        VARIABLE QUANTITY
# 00000000              00
# 00000040              40
# 0000007F              7F
# 00000080             81 00
# 00002000             C0 00
# 00003FFF             FF 7F
# 00004000           81 80 00
# 00100000           C0 80 00
# 001FFFFF           FF FF 7F
# 00200000          81 80 80 00
# 08000000          C0 80 80 00
# 0FFFFFFF          FF FF FF 7F
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
# a ValueError if the sequence to decode or encode is incomplete. The tests will
# only pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
# # if the sequence is incomplete
# raise ValueError("incomplete sequence")
#
# References:
# - https://exercism.org/tracks/python/exercises/variable-length-quantity
# - https://splice.com/
#


class VariableLengthQuantity:
    def __init__(self) -> None:
        self.__encoded__: list[int] = []
        self.__decoded__: list[int] = []

    def encode(self, numbers: list[int]) -> list[int]:
        self.__encoded__ = []
        for number in numbers:
            if number < 0:
                raise ValueError("negative number")
            elif number > 0x1FFFFFFF:
                raise ValueError("number too large")
            elif number == 0:
                self.__encoded__.append(0)
            else:
                encoded: list[int] = []
                while number > 0:
                    encoded.append(number & 0x7F)
                    number >>= 7
                encoded.reverse()
                for i in range(len(encoded)):
                    if i < len(encoded) - 1:
                        encoded[i] |= 0x80
                self.__encoded__.extend(encoded)
        return self.__encoded__

    def decode(self, sequence: list[int]) -> list[int]:
        self.__decoded__ = []
        number: int = 0
        for i, byte in enumerate(sequence):
            if byte < 0:
                raise ValueError("byte is negative")
            number = (number << 7) | (byte & 0x7F)
            if not byte & 0x80:
                self.__decoded__.append(number)
                number = 0
            elif i == len(sequence) - 1:
                raise ValueError("incomplete sequence")
        return self.__decoded__
