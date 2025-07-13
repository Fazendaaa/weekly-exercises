from pytest import raises
from weekly_exercises.SGFParsing import SGF


def test_empty_input() -> None:
    with raises(ValueError, match="tree missing"):
        SGF().parse("")


def test_tree_with_no_nodes() -> None:
    with raises(ValueError, match="tree with no nodes"):
        SGF().parse("()")


def test_node_without_tree() -> None:
    with raises(ValueError, match="tree missing"):
        SGF().parse(";")


def test_node_without_properties() -> None:
    assert SGF().parse("(;)") == {
        "properties": {},
        "children": [],
    }


def test_single_node_tree() -> None:
    assert SGF().parse("(;A[B])") == {
        "properties": {
            "A": [
                "B",
            ],
        },
        "children": [],
    }


def test_multiple_properties() -> None:
    assert SGF().parse("(;A[b]C[d])") == {
        "properties": {
            "A": [
                "b",
            ],
            "C": [
                "d",
            ],
        },
        "children": [],
    }


def test_properties_without_delimiter() -> None:
    with raises(ValueError, match="properties without delimiter"):
        SGF().parse("(;A)")


def test_all_lowercase_property() -> None:
    with raises(ValueError, match="property must be in uppercase"):
        SGF().parse("(;a[b])")


def test_upper_and_lowercase_property() -> None:
    with raises(ValueError, match="property must be in uppercase"):
        SGF().parse("(;Aa[b])")


def test_two_nodes() -> None:
    assert SGF().parse("(;A[B];B[C])") == {
        "properties": {
            "A": [
                "B",
            ],
        },
        "children": [
            {
                "B": [
                    "C",
                ],
            },
        ],
    }


def test_two_child_trees() -> None:
    assert SGF().parse("(;A[B](;B[C])(;C[D]))") == {
        "properties": {
            "A": [
                "B",
            ],
        },
        "children": [
            {
                "B": ["C"],
            },
            {
                "C": ["D"],
            },
        ],
    }


def test_multiple_property_values() -> None:
    assert SGF().parse("(;A[b][c][d])") == {
        "properties": {
            "A": [
                "b",
                "c",
                "d",
            ],
        },
        "children": [],
    }


def test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces() -> (
    None
):
    assert SGF().parse("(;A[hello\t\tworld])") == {
        "properties": {
            "A": [
                "hello\t\tworld",
            ],
        },
        "children": [],
    }


def test_within_property_values_newlines_remain_as_newlines() -> None:
    assert SGF().parse("(;A[hello\n\nworld])") == {
        "properties": {
            "A": [
                "hello\n\nworld",
            ],
        },
        "children": [],
    }


def test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket() -> (
    None
):
    assert SGF().parse("(;A[\\]])") == {
        "properties": {
            "A": [
                "]",
            ],
        },
        "children": [],
    }


def test_escaped_backslash_in_property_value_becomes_just_a_backslash() -> None:
    assert SGF().parse("(;A[\\\\])") == {
        "properties": {
            "A": [
                "\\",
            ],
        },
        "children": [],
    }


def test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped() -> None:
    assert SGF().parse("(;A[x[y\\]z][foo]B[bar];C[baz])") == {
        "properties": {
            "A": [
                "x[y]z",
                "foo",
            ],
            "B": [
                "bar",
            ],
        },
        "children": [
            {
                "C": [
                    "baz",
                ]
            },
        ],
    }


def test_semicolon_in_property_value_doesn_t_need_to_be_escaped() -> None:
    assert SGF().parse("(;A[a;b][foo]B[bar];C[baz])") == {
        "properties": {
            "A": [
                "a;b",
                "foo",
            ],
            "B": [
                "bar",
            ],
        },
        "children": [
            {
                "C": [
                    "baz",
                ],
            },
        ],
    }


def test_parentheses_in_property_value_don_t_need_to_be_escaped() -> None:
    assert SGF().parse("(;A[x(y)z][foo]B[bar];C[baz])") == {
        "properties": {
            "A": [
                "x(y)z",
                "foo",
            ],
            "B": [
                "bar",
            ],
        },
        "children": [
            {
                "C": [
                    "baz",
                ],
            },
        ],
    }


def test_escaped_tab_in_property_value_is_converted_to_space() -> None:
    assert SGF().parse("(;A[hello\\\tworld])") == {
        "properties": {
            "A": [
                "hello world",
            ],
        },
        "children": [],
    }


def test_escaped_newline_in_property_value_is_converted_to_nothing_at_all() -> None:
    assert SGF().parse("(;A[hello\\\nworld])") == {
        "properties": {
            "A": [
                "helloworld",
            ],
        },
        "children": [],
    }


def test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace() -> None:
    assert SGF().parse("(;A[\\t = t and \\n = n])") == {
        "properties": {
            "A": [
                "t = t and n = n",
            ],
        },
        "children": [],
    }


def test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value() -> (
    None
):
    assert SGF().parse("(;A[\\]b\nc\\\nd\t\te\\\\ \\\n\\]])") == {
        "properties": {
            "A": [
                "]b\ncd  e\\ ]",
            ],
        },
        "children": [],
    }
