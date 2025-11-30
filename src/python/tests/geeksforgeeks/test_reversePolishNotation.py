from weekly_exercises.geeksforgeeks.reversePolishNotation import ReversePolishNotation


def test_geeksforgeeks_examples() -> None:
    assert ReversePolishNotation.eval(["2", "1", "+", "3", "*"]) == 9, "Output is not 9"
    assert (
        ReversePolishNotation.eval(["4", "13", "5", "/", "+"]) == 6
    ), "Output is not 6"
    assert (
        ReversePolishNotation.eval(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    ), "Output is not 22"
