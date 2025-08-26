from pytest import raises
from weekly_exercises.exercism.goCounting import Go, Stone


def test_black_corner_territory_on_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )
    stone, territory = board.territory(x=0, y=1)

    assert stone == Stone.BLACK
    assert territory == {
        (0, 0),
        (0, 1),
        (1, 0),
    }


def test_white_center_territory_on_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )
    stone, territory = board.territory(x=2, y=3)

    assert stone == Stone.WHITE
    assert territory == {
        (2, 3),
    }


def test_open_corner_territory_on_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )
    stone, territory = board.territory(x=1, y=4)

    assert stone == Stone.NONE
    assert territory == {
        (0, 3),
        (0, 4),
        (1, 4),
    }


def test_a_stone_and_not_a_territory_on_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )
    stone, territory = board.territory(x=1, y=1)

    assert stone == Stone.NONE
    assert territory == set()


def test_invalid_because_x_is_too_low_for_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=-1, y=1)


def test_invalid_because_x_is_too_high_for_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=5, y=1)


def test_invalid_because_y_is_too_low_for_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=1, y=-1)


def test_invalid_because_y_is_too_high_for_5x5_board() -> None:
    board = Go(
        [
            "  B  ",
            " B B ",
            "B W B",
            " W W ",
            "  W  ",
        ]
    )

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=1, y=5)


def test_one_territory_is_the_whole_board() -> None:
    board = Go(
        [
            " ",
        ]
    )
    territories = board.territories()

    assert territories[Stone.BLACK] == set()
    assert territories[Stone.WHITE] == set()
    assert territories[Stone.NONE] == {
        (0, 0),
    }


def test_two_territory_rectangular_board() -> None:
    board = Go(
        [
            " BW ",
            " BW ",
        ]
    )
    territories = board.territories()

    assert territories[Stone.BLACK] == {
        (0, 0),
        (0, 1),
    }
    assert territories[Stone.WHITE] == {
        (3, 0),
        (3, 1),
    }
    assert territories[Stone.NONE] == set()


def test_two_region_rectangular_board() -> None:
    board = Go(
        [
            " B ",
        ]
    )
    territories = board.territories()

    assert territories[Stone.BLACK] == {
        (0, 0),
        (2, 0),
    }
    assert territories[Stone.WHITE] == set()
    assert territories[Stone.NONE] == set()
