#                               Instructions
#
# Implement run-length encoding and decoding.
#
# Run-length encoding (RLE) is a simple form of data compression, where runs
# (consecutive data elements) are replaced by just one data value and count.
#
# For example we can represent the original 53 characters with only 13.
#
# "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
#
# RLE allows the original data to be perfectly reconstructed from the compressed
# data, which makes it a lossless data compression.
#
# "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
#
# For simplicity, you can assume that the unencoded string will only contain the
# letters A through Z (either lower or upper case) and whitespace. This way data
# to be encoded will never contain any numbers and numbers inside data to be
# decoded always represent the count for the following character.
#
# Reference:
#   - https://exercism.org/tracks/r/exercises/run-length-encoding
#


def encode(text: str) -> str:
    if not text:
        return ""

    result: list[str] = []
    count = 1
    prev = text[0]

    for current in text[1:] + " ":
        if current == prev:
            count += 1
        else:
            if 1 != count:
                result.append(str(count))

            result.append(prev)
            prev = current
            count = 1

    return "".join(result)


def decode(text: str) -> str:
    result: list[str] = []
    count = ""

    for char in text:
        if char.isdigit():
            count += char
        else:
            if count:
                result.append(char * int(count))
                count = ""
            else:
                result.append(char)

    return "".join(result)
