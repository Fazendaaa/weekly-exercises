from re import match

from weekly_exercises.exercism.simpleCipher import Cipher


def test_can_encode_random_key() -> None:
    cipher = Cipher()
    plaintext = "aaaaaaaaaa"

    assert cipher.encode(plaintext) == cipher.key[0 : len(plaintext)]


def test_can_decode_random_key() -> None:
    cipher = Cipher()

    assert cipher.decode(cipher.key[0 : len("aaaaaaaaaa")]) == "aaaaaaaaaa"


def test_is_reversible_random_key() -> None:
    cipher = Cipher()
    plaintext = "abcdefghij"

    assert cipher.decode(cipher.encode(plaintext)) == plaintext


def test_key_is_made_only_of_lowercase_letters() -> None:
    assert match("^[a-z]+$", Cipher().key) is not None


def test_can_encode_with_given_key() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "aaaaaaaaaa"

    assert cipher.encode(plaintext) == cipher.key


def test_can_decode_with_given_key() -> None:
    cipher = Cipher("abcdefghij")

    assert cipher.decode(cipher.key) == "aaaaaaaaaa"


def test_is_reversible_with_given_key() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "abcdefghij"

    assert cipher.decode(cipher.encode(plaintext)) == plaintext


def test_can_double_shift_encode() -> None:
    cipher = Cipher("iamapandabear")
    plaintext = "iamapandabear"

    assert cipher.encode(plaintext) == "qayaeaagaciai"


def test_can_wrap_on_encode() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "zzzzzzzzzz"

    assert cipher.encode(plaintext) == "zabcdefghi"


def test_can_wrap_on_decode() -> None:
    cipher = Cipher("abcdefghij")

    assert cipher.decode("zabcdefghi") == "zzzzzzzzzz"


def test_can_encode_messages_longer_than_the_key() -> None:
    cipher = Cipher("abc")
    plaintext = "iamapandabear"

    assert cipher.encode(plaintext) == "iboaqcnecbfcr"


def test_can_decode_messages_longer_than_the_key() -> None:
    cipher = Cipher("abc")

    assert cipher.decode("iboaqcnecbfcr") == "iamapandabear"
