from weekly_exercises.exercism.zipper import Zipper


def test_data_is_retained() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).to_tree() == expected


def test_left_right_and_value() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().right().value() == 3


def test_dead_end() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert not Zipper.from_tree(initial).left().left()


def test_tree_from_deep_focus() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().right().to_tree() == expected


def test_traversing_up_from_top() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert not Zipper.from_tree(initial).up()


def test_left_right_and_up() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert (
        Zipper.from_tree(initial).left().up().right().up().left().right().value() == 3
    )


def test_test_ability_to_descend_multiple_levels_and_return() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().right().up().up().value() == 1


def test_set_value() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 5,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().set_value(5).to_tree() == expected


def test_set_value_after_traversing_up() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 5,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert (
        Zipper.from_tree(initial).left().right().up().set_value(5).to_tree() == expected
    )


def test_set_left_with_leaf() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": {
                "value": 5,
                "left": None,
                "right": None,
            },
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert (
        Zipper.from_tree(initial)
        .left()
        .set_left(
            {
                "value": 5,
                "left": None,
                "right": None,
            }
        )
        .to_tree()
        == expected
    )


def test_set_right_with_null() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": None,
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().set_right(None).to_tree() == expected


def test_set_right_with_subtree() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 6,
            "left": {
                "value": 7,
                "left": None,
                "right": None,
            },
            "right": {
                "value": 8,
                "left": None,
                "right": None,
            },
        },
    }

    assert (
        Zipper.from_tree(initial)
        .set_right(
            {
                "value": 6,
                "left": {
                    "value": 7,
                    "left": None,
                    "right": None,
                },
                "right": {
                    "value": 8,
                    "left": None,
                    "right": None,
                },
            }
        )
        .to_tree()
        == expected
    )


def test_set_value_on_deep_focus() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 5,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert Zipper.from_tree(initial).left().right().set_value(5).to_tree() == expected


def test_different_paths_to_same_zipper() -> None:
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }
    final = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None,
            },
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None,
        },
    }

    assert (
        Zipper.from_tree(initial).left().up().right().to_tree()
        == Zipper.from_tree(final).right().to_tree()
    )
