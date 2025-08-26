from typing import Any, Callable, Optional, TypeVar, cast

import pytest
from weekly_exercises.exercism.matchingBrackets import ENGINES, MatchingBrackets

F = TypeVar("F", bound=Callable[..., Any])
T = TypeVar("T")


def parametrize_all(
    argnames: str,
    argvalues: list[tuple[Any, ...]],
    ids: Optional[list[str]] = None,
    indirect: bool = False,
    scope: str = "function",
) -> Callable[[F], F]:
    """
    Decorator factory to apply same parametrization to multiple functions.

    Args:
        argnames: Comma-separated string of parameter names
        argvalues: List of tuples with test data
        ids: Optional list of test IDs
        indirect: Whether parameters should be passed to fixtures
        scope: The scope of the parametrization

    Returns:
        A decorator that applies the parametrization
    """

    def decorator(func: F) -> F:
        decorated_func = pytest.mark.parametrize(
            argnames, argvalues, ids=ids, indirect=indirect, scope=scope
        )(func)
        return decorated_func

    return decorator


ENGINES_TEST = [
    "stack",
    "recursive",
    "state",
]


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_square_brackets(engine: ENGINES) -> None:
    assert MatchingBrackets("[]").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_empty_string(engine: ENGINES) -> None:
    assert MatchingBrackets("").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_unpaired_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("[[").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_wrong_ordered_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("}{").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_wrong_closing_bracket(engine: ENGINES) -> None:
    assert not MatchingBrackets("{]").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_with_whitespace(engine: ENGINES) -> None:
    assert MatchingBrackets("{ }").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_partially_paired_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("{[])").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_simple_nested_brackets(engine: ENGINES) -> None:
    assert MatchingBrackets("{[]}").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_several_paired_brackets(engine: ENGINES) -> None:
    assert MatchingBrackets("{}[]").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_and_nested_brackets(engine: ENGINES) -> None:
    assert MatchingBrackets("([{}({}[])])").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_unopened_closing_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("{[)][]}").isPaired(engine)


def test_unpaired_and_nested_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("([{])").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_and_wrong_nested_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("[({]})").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_and_wrong_nested_brackets_but_innermost_are_correct(
    engine: ENGINES,
) -> None:
    assert not MatchingBrackets("[({}])").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_paired_and_incomplete_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("{}[").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_too_many_closing_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("[]]").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_early_unexpected_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets(")()").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_early_mismatched_brackets(engine: ENGINES) -> None:
    assert not MatchingBrackets("{)()").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_math_expression(engine: ENGINES) -> None:
    assert MatchingBrackets("(((185 + 223.85) * 15) - 543)/2").isPaired(engine)


@parametrize_all(
    "engine",
    ENGINES_TEST,
)
def test_complex_latex_expression(engine: ENGINES) -> None:
    assert MatchingBrackets(
        "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{x} &... x^2 \\end{array}\\right)"
    ).isPaired(engine)
