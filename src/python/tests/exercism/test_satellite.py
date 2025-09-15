from pytest import raises
from weekly_exercises.exercism.satellite import Traversals, treeFromTraversals


def test_empty_tree() -> None:
    preorder: list[str] = []
    inorder: list[str] = []
    expected: Traversals = {}

    assert treeFromTraversals(preorder, inorder) == expected


def test_tree_with_one_item() -> None:
    preorder = [
        "a",
    ]
    inorder = [
        "a",
    ]
    expected: Traversals = {
        "value": "a",
        "left": {},
        "right": {},
    }

    assert treeFromTraversals(preorder, inorder) == expected


def test_tree_with_many_items() -> None:
    preorder = [
        "a",
        "i",
        "x",
        "f",
        "r",
    ]
    inorder = [
        "i",
        "a",
        "f",
        "x",
        "r",
    ]
    expected: Traversals = {
        "value": "a",
        "left": {
            "value": "i",
            "left": {},
            "right": {},
        },
        "right": {
            "value": "x",
            "left": {
                "value": "f",
                "left": {},
                "right": {},
            },
            "right": {
                "value": "r",
                "left": {},
                "right": {},
            },
        },
    }

    assert treeFromTraversals(preorder, inorder) == expected


def test_reject_traversals_of_different_length() -> None:
    preorder = [
        "a",
        "b",
    ]
    inorder = [
        "b",
        "a",
        "r",
    ]

    with raises(ValueError, match="traversals must have the same length"):
        treeFromTraversals(preorder, inorder)


def test_reject_inconsistent_traversals_of_same_length() -> None:
    preorder = [
        "x",
        "y",
        "z",
    ]
    inorder = [
        "a",
        "b",
        "c",
    ]

    with raises(ValueError, match="traversals must have the same elements"):
        treeFromTraversals(preorder, inorder)


def test_reject_traversals_with_repeated_items() -> None:
    preorder = [
        "a",
        "b",
        "a",
    ]
    inorder = [
        "b",
        "a",
        "a",
    ]

    with raises(ValueError, match="traversals must contain unique items"):
        treeFromTraversals(preorder, inorder)
