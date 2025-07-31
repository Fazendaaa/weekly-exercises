from weekly_exercises.exercism.listOps import List


def test_append_empty_lists() -> None:
    assert List().append([]) == []
    assert List().append([]) == List()


def test_append_list_to_empty_list() -> None:
    assert List().append([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_append_empty_list_to_list() -> None:
    assert List([1, 2, 3, 4]).append([]) == [1, 2, 3, 4]


def test_append_non_empty_lists() -> None:
    assert List([1, 2]).append([2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]


def test_concat_empty_list() -> None:
    assert List().concat([]) == []


def test_concat_list_of_lists() -> None:
    assert List().concat([[1, 2], [3], [], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]


def test_concat_list_of_nested_lists() -> None:
    assert List().concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]) == [
        [1],
        [2],
        [3],
        [],
        [4, 5, 6],
    ]


def test_filter_empty_list() -> None:
    assert List().filter(lambda x: x % 2 == 1) == []


def test_filter_non_empty_list() -> None:
    assert List([1, 2, 3, 5]).filter(lambda x: x % 2 == 1) == [1, 3, 5]


def test_length_empty_list() -> None:
    assert List().length() == 0


def test_length_non_empty_list() -> None:
    assert List([1, 2, 3, 4]).length() == 4


def test_map_empty_list() -> None:
    assert List().map(lambda item: item + 1) == []


def test_map_non_empty_list() -> None:
    assert List([1, 3, 5, 7]).map(lambda item: item + 1) == [2, 4, 6, 8]


def test_foldl_empty_list() -> None:
    assert List().foldl(lambda accumulator, item: accumulator * item, 2) == 2


def test_foldl_direction_independent_function_applied_to_non_empty_list() -> None:
    assert (
        List([1, 2, 3, 4]).foldl(lambda accumulator, item: accumulator + item, 5) == 15
    )


def test_foldl_direction_dependent_function_applied_to_non_empty_list() -> None:
    assert (
        List([1, 2, 3, 4]).foldl(lambda accumulator, item: item / accumulator, 24) == 64
    )


def test_foldr_empty_list() -> None:
    assert List().foldr(lambda accumulator, item: accumulator * item, 2) == 2


def test_foldr_direction_independent_function_applied_to_non_empty_list() -> None:
    assert (
        List([1, 2, 3, 4]).foldr(lambda accumulator, item: accumulator + item, 5) == 15
    )


def test_foldr_direction_dependent_function_applied_to_non_empty_list() -> None:
    assert (
        List([1, 2, 3, 4]).foldr(lambda accumulator, item: accumulator / item, 24) == 9
    )


def test_reverse_empty_list() -> None:
    assert List().reverse() == []


def test_reverse_non_empty_list() -> None:
    assert List([1, 3, 5, 7]).reverse() == [7, 5, 3, 1]


def test_reverse_list_of_lists_is_not_flattened() -> None:
    assert List([[1, 2], [3], [], [4, 5, 6]]).reverse() == [[4, 5, 6], [], [3], [1, 2]]


def test_foldr_foldr_add_string() -> None:
    assert (
        List(["e", "x", "e", "r", "c", "i", "s", "m"]).foldr(
            lambda accumulator, item: accumulator + item, "!"
        )
        == "exercism!"
    )


def test_reverse_reverse_mixed_types() -> None:
    assert List(["xyz", 4.0, "cat", 1]).reverse() == [1, "cat", 4.0, "xyz"]
