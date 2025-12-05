# Simple Cipher
#
# Instructions
#
# Create an implementation of the Vigenère cipher. The Vigenère cipher is a
# simple substitution cipher.
#
# Cipher terminology
#
# A cipher is an algorithm used to encrypt, or encode, a string. The unencrypted
# string is called the plaintext and the encrypted string is called the
# ciphertext. Converting plaintext to ciphertext is called encoding while the
# reverse is called decoding.
#
# In a substitution cipher, each plaintext letter is replaced with a ciphertext
# letter which is computed with the help of a key. (Note, it is possible for
# replacement letter to be the same as the original letter.)
#
# Encoding details
#
# In this cipher, the key is a series of lowercase letters, such as "abcd". Each
# letter of the plaintext is shifted or rotated by a distance based on a
# corresponding letter in the key. An "a" in the key means a shift of 0 (that
# is, no shift). A "b" in the key means a shift of 1. A "c" in the key means a
# shift of 2, and so on.
#
# The first letter of the plaintext uses the first letter of the key, the second
# letter of the plaintext uses the second letter of the key and so on. If you
# run out of letters in the key before you run out of letters in the plaintext,
# start over from the start of the key again.
#
# If the key only contains one letter, such as "dddddd", then all letters of the
# plaintext are shifted by the same amount (three in this example), which would
# make this the same as a rotational cipher or shift cipher (sometimes called a
# Caesar cipher). For example, the plaintext "iamapandabear" would become
# "ldpdsdqgdehdu".
#
# If the key only contains the letter "a" (one or more times), the shift
# distance is zero and the ciphertext is the same as the plaintext.
#
# Usually the key is more complicated than that, though! If the key is "abcd"
# then letters of the plaintext would be shifted by a distance of 0, 1, 2, and
# 3. If the plaintext is "hello", we need 5 shifts so the key would wrap around,
# giving shift distances of 0, 1, 2, 3, and 0. Applying those shifts to the
# letters of "hello" we get "hfnoo".
#
# Random keys
#
# If no key is provided, generate a key which consists of at least 100 random
# lowercase letters from the Latin alphabet.
#
# Python, as of version 3.6, includes two different random modules.
#
# The module called random is pseudo-random, meaning it does not generate true
# randomness, but follows an algorithm that simulates randomness. Since random
# numbers are generated through a known algorithm, they are not truly random.
#
# The random module is not correctly suited for cryptography and should not be
# used, precisely because it is pseudo-random.
#
# For this reason, in version 3.6, Python introduced the secrets module, which
# generates cryptographically strong random numbers that provide the greater
# security required for cryptography.
#
# Since this is only an exercise, random is fine to use, but note that it would
# be very insecure if actually used for cryptography.
#
# References:
#     - https://exercism.org/tracks/python/exercises/simple-cipher
#

from itertools import cycle
from random import choice
from string import ascii_lowercase


class Cipher:
    """A class implementing the Vigenère cipher for text encryption and decryption.

    The Vigenère cipher is a polyalphabetic substitution cipher that uses a key to
    shift each letter in the plaintext by varying amounts.

    Attributes:
        key (str): The encryption/decryption key. If not provided, a random 100-character
            key is generated using lowercase letters.
    """

    def __init__(
        self,
        key: str = "",
    ) -> None:
        """Initialize a new Cipher instance.

        Args:
            key (str, optional): The encryption/decryption key. Defaults to an empty string,
                in which case a random 100-character key is generated.
        """
        self.key = key if key else "".join(choice(ascii_lowercase) for _ in range(100))

    def __repr__(self) -> str:
        """Return a string representation of the Cipher instance.

        Returns:
            str: A string showing the class name and encryption key.
        """
        return f"Cipher({self.key})"

    def encode(
        self,
        text: str,
    ) -> str:
        """Encode plaintext using the Vigenère cipher.

        Each letter in the plaintext is shifted based on the corresponding letter in the key.
        The key is repeated if it's shorter than the plaintext.

        Args:
            text (str): The plaintext to encode.

        Returns:
            str: The encoded ciphertext.
        """
        result: list[str] = []

        for char, key in zip(text.lower(), cycle(self.key)):
            shift = ord(key) - ord("a")
            newChar = ord(char) + shift

            result.append(chr(newChar - 26 if newChar > ord("z") else newChar))

        return "".join(result)

    def decode(
        self,
        text: str,
    ) -> str:
        """Decode ciphertext back to plaintext using the Vigenère cipher.

        Each letter in the ciphertext is shifted back based on the corresponding letter
        in the key. The key is repeated if it's shorter than the ciphertext.

        Args:
            text (str): The ciphertext to decode.

        Returns:
            str: The decoded plaintext.
        """
        result: list[str] = []

        for char, key_char in zip(text.lower(), cycle(self.key)):
            shift = ord(key_char) - ord("a")
            newChar = ord(char) - shift

            result.append(chr(newChar + 26 if newChar < ord("a") else newChar))

        return "".join(result)
