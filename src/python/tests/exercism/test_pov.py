from pytest import raises
from weekly_exercises.exercism.pov import Tree


def test_results_in_the_same_tree_if_the_input_tree_is_a_singleton() -> None:
    tree = Tree("x")
    expected = Tree("x")

    assert tree.from_pov("x") == expected


def test_can_reroot_a_tree_with_a_parent_and_one_sibling() -> None:
    tree = Tree(
        "parent",
        [
            Tree("x"),
            Tree("sibling"),
        ],
    )
    expected = Tree(
        "x",
        [
            Tree(
                "parent",
                [
                    Tree("sibling"),
                ],
            ),
        ],
    )

    assert tree.from_pov("x") == expected


def test_can_reroot_a_tree_with_a_parent_and_many_siblings() -> None:
    tree = Tree(
        "parent",
        [
            Tree("a"),
            Tree("x"),
            Tree("b"),
            Tree("c"),
        ],
    )
    expected = Tree(
        "x",
        [
            Tree(
                "parent",
                [
                    Tree("a"),
                    Tree("b"),
                    Tree("c"),
                ],
            )
        ],
    )

    assert tree.from_pov("x") == expected


def test_can_reroot_a_tree_with_new_root_deeply_nested_in_tree() -> None:
    tree = Tree(
        "level-0",
        [
            Tree(
                "level-1",
                [
                    Tree(
                        "level-2",
                        [
                            Tree(
                                "level-3",
                                [
                                    Tree("x"),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
    expected = Tree(
        "x",
        [
            Tree(
                "level-3",
                [
                    Tree(
                        "level-2",
                        [
                            Tree(
                                "level-1",
                                [
                                    Tree("level-0"),
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )

    assert tree.from_pov("x") == expected


def test_moves_children_of_the_new_root_to_same_level_as_former_parent() -> None:
    tree = Tree(
        "parent",
        [
            Tree(
                "x",
                [
                    Tree("kid-0"),
                    Tree("kid-1"),
                ],
            ),
        ],
    )
    expected = Tree(
        "x",
        [
            Tree("kid-0"),
            Tree("kid-1"),
            Tree("parent"),
        ],
    )

    assert tree.from_pov("x") == expected


def test_can_reroot_a_complex_tree_with_cousins() -> None:
    tree = Tree(
        "grandparent",
        [
            Tree(
                "parent",
                [
                    Tree(
                        "x",
                        [
                            Tree("kid-0"),
                            Tree("kid-1"),
                        ],
                    ),
                    Tree("sibling-0"),
                    Tree("sibling-1"),
                ],
            ),
            Tree(
                "uncle",
                [
                    Tree("cousin-0"),
                    Tree("cousin-1"),
                ],
            ),
        ],
    )
    expected = Tree(
        "x",
        [
            Tree("kid-1"),
            Tree("kid-0"),
            Tree(
                "parent",
                [
                    Tree("sibling-0"),
                    Tree("sibling-1"),
                    Tree(
                        "grandparent",
                        [
                            Tree(
                                "uncle",
                                [
                                    Tree("cousin-0"),
                                    Tree("cousin-1"),
                                ],
                            )
                        ],
                    ),
                ],
            ),
        ],
    )

    assert tree.from_pov("x") == expected


def test_errors_if_target_does_not_exist_in_a_singleton_tree() -> None:
    tree = Tree("x")

    with raises(ValueError, match="Tree could not be reoriented"):
        tree.from_pov("nonexistent")


def test_errors_if_target_does_not_exist_in_a_large_tree() -> None:
    tree = Tree(
        "parent",
        [
            Tree(
                "x",
                [
                    Tree("kid-0"),
                    Tree("kid-1"),
                ],
            ),
            Tree("sibling-0"),
            Tree("sibling-1"),
        ],
    )

    with raises(ValueError, match="Tree could not be reoriented"):
        tree.from_pov("nonexistent")


def test_can_find_path_to_parent() -> None:
    tree = Tree(
        "parent",
        [
            Tree("x"),
            Tree("sibling"),
        ],
    )
    expected = ["x", "parent"]

    assert tree.path_to("x", "parent") == expected


def test_can_find_path_to_sibling() -> None:
    tree = Tree(
        "parent",
        [
            Tree("a"),
            Tree("x"),
            Tree("b"),
            Tree("c"),
        ],
    )
    expected = ["x", "parent", "b"]

    assert tree.path_to("x", "b") == expected


def test_can_find_path_to_cousin() -> None:
    tree = Tree(
        "grandparent",
        [
            Tree(
                "parent",
                [
                    Tree(
                        "x",
                        [
                            Tree("kid-0"),
                            Tree("kid-1"),
                        ],
                    ),
                    Tree("sibling-0"),
                    Tree("sibling-1"),
                ],
            ),
            Tree(
                "uncle",
                [
                    Tree("cousin-0"),
                    Tree("cousin-1"),
                ],
            ),
        ],
    )
    expected = ["x", "parent", "grandparent", "uncle", "cousin-1"]

    assert tree.path_to("x", "cousin-1") == expected


def test_can_find_path_not_involving_root() -> None:
    tree = Tree(
        "grandparent",
        [
            Tree(
                "parent",
                [
                    Tree("x"),
                    Tree("sibling-0"),
                    Tree("sibling-1"),
                ],
            ),
        ],
    )
    expected = ["x", "parent", "sibling-1"]

    assert tree.path_to("x", "sibling-1") == expected


def test_can_find_path_from_nodes_other_than_x() -> None:
    tree = Tree(
        "parent",
        [
            Tree("a"),
            Tree("x"),
            Tree("b"),
            Tree("c"),
        ],
    )
    expected = ["a", "parent", "c"]

    assert tree.path_to("a", "c") == expected


def test_errors_if_destination_does_not_exist() -> None:
    tree = Tree(
        "parent",
        [
            Tree(
                "x",
                [
                    Tree("kid-0"),
                    Tree("kid-1"),
                ],
            ),
            Tree("sibling-0"),
            Tree("sibling-1"),
        ],
    )

    with raises(ValueError, match="No path found"):
        tree.path_to("x", "nonexistent")


def test_errors_if_source_does_not_exist() -> None:
    tree = Tree(
        "parent",
        [
            Tree(
                "x",
                [
                    Tree("kid-0"),
                    Tree("kid-1"),
                ],
            ),
            Tree("sibling-0"),
            Tree("sibling-1"),
        ],
    )

    with raises(ValueError, match="Tree could not be reoriented"):
        tree.path_to("nonexistent", "x")
