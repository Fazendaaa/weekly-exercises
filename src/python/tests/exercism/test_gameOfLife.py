from weekly_exercises.exercism.gameOfLife import GameOfLife


def test_live_cells_with_zero_live_neighbors_die() -> None:
    input_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_live_cells_with_only_one_live_neighbor_die() -> None:
    input_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_live_cells_with_two_live_neighbors_stay_alive() -> None:
    input_grid = [
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
    ]
    expected = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_live_cells_with_three_live_neighbors_stay_alive() -> None:
    input_grid = [
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 0],
    ]
    expected = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_dead_cells_with_three_live_neighbors_become_alive() -> None:
    input_grid = [
        [1, 1, 0],
        [0, 0, 0],
        [1, 0, 0],
    ]
    expected = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_live_cells_with_four_or_more_neighbors_die() -> None:
    input_grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    expected = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected


def test_bigger_matrix() -> None:
    input_grid = [
        [1, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
    ]
    expected = [
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
    ]
    game = GameOfLife(input_grid)

    game.tick()

    assert game.status() == expected
