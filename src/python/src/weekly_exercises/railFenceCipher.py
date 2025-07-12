#                               Instructions
#
# Implement encoding and decoding for the rail fence cipher.
#
# The Rail Fence cipher is a form of transposition cipher that gets its name
# from the way in which it's encoded. It was already used by the ancient Greeks.
#
# In the Rail Fence cipher, the message is written downwards on successive
# "rails" of an imaginary fence, then moving up when we get to the bottom (like
# a zig-zag). Finally the message is then read off in rows.
#
# For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT
# ONCE", the cipherer writes out:
#
#   W . . . E . . . C . . . R . . . L . . . T . . . E
#   . E . R . D . S . O . E . E . F . E . A . O . C .
#   . . A . . . I . . . V . . . D . . . E . . . N . .
#
# Then reads off:
#
#   WECRLTEERDSOEEFEAOCAIVDEN
#
# To decrypt a message you take the zig-zag shape and fill the ciphertext along
# he rows.
#
#   ? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
#   . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
#   . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# The first row has seven spots that can be filled with "WECRLTE".
#
#   W . . . E . . . C . . . R . . . L . . . T . . . E
#   . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
#   . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# Now the 2nd row takes "ERDSOEEFEAOC".
#
#   W . . . E . . . C . . . R . . . L . . . T . . . E
#   . E . R . D . S . O . E . E . F . E . A . O . C .
#   . . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
#
# Leaving "AIVDEN" for the last row.
#
#   W . . . E . . . C . . . R . . . L . . . T . . . E
#   . E . R . D . S . O . E . E . F . E . A . O . C .
#   . . A . . . I . . . V . . . D . . . E . . . N . .
#
# If you now read along the zig-zag shape you can read the original message.
#
# Source
# - https://en.wikipedia.org/wiki/Transposition_cipher#Rail_Fence_cipher
# - https://exercism.org/tracks/python/exercises/rail-fence-cipher
#


class RailFence:
    def __init__(self) -> None:
        pass

    def encode(self, message: str, rails: int) -> str:
        if not message:
            return ""

        if rails == 1:
            return message

        encoded: list[str] = [""] * rails
        rail: int = 0
        direction: int = 1

        for char in message:
            encoded[rail] += char
            rail += direction

            if rail == 0 or rail == rails - 1:
                direction *= -1

        return "".join(encoded)

    def decode(self, message: str, rails: int) -> str:
        if not message:
            return ""

        if rails == 1:
            return message

        decoded: list[str] = [""] * len(message)
        rail: int = 0
        direction: int = 1

        for i in range(len(message)):
            decoded[i] = message[rail]
            rail += direction

            if rail == 0 or rail == rails - 1:
                direction *= -1

        return "".join(decoded)
