from weekly_exercises.exercism.diamond import Diamond


def test_degenerate_case_with_a_single_a_row() -> None:
    assert [
        "A",
    ] == Diamond("A").make_diamond()


def test_degenerate_case_with_no_row_containing_3_distinct_groups_of_spaces() -> None:
    assert [
        " A ",
        "B B",
        " A ",
    ] == Diamond("B").make_diamond()


def test_smallest_non_degenerate_case_with_odd_diamond_side_length() -> None:
    assert [
        "  A  ",
        " B B ",
        "C   C",
        " B B ",
        "  A  ",
    ] == Diamond("C").make_diamond()


def test_smallest_non_degenerate_case_with_even_diamond_side_length() -> None:
    assert [
        "   A   ",
        "  B B  ",
        " C   C ",
        "D     D",
        " C   C ",
        "  B B  ",
        "   A   ",
    ] == Diamond("D").make_diamond()


def test_largest_possible_diamond() -> None:
    assert [
        "                         A                         ",
        "                        B B                        ",
        "                       C   C                       ",
        "                      D     D                      ",
        "                     E       E                     ",
        "                    F         F                    ",
        "                   G           G                   ",
        "                  H             H                  ",
        "                 I               I                 ",
        "                J                 J                ",
        "               K                   K               ",
        "              L                     L              ",
        "             M                       M             ",
        "            N                         N            ",
        "           O                           O           ",
        "          P                             P          ",
        "         Q                               Q         ",
        "        R                                 R        ",
        "       S                                   S       ",
        "      T                                     T      ",
        "     U                                       U     ",
        "    V                                         V    ",
        "   W                                           W   ",
        "  X                                             X  ",
        " Y                                               Y ",
        "Z                                                 Z",
        " Y                                               Y ",
        "  X                                             X  ",
        "   W                                           W   ",
        "    V                                         V    ",
        "     U                                       U     ",
        "      T                                     T      ",
        "       S                                   S       ",
        "        R                                 R        ",
        "         Q                               Q         ",
        "          P                             P          ",
        "           O                           O           ",
        "            N                         N            ",
        "             M                       M             ",
        "              L                     L              ",
        "               K                   K               ",
        "                J                 J                ",
        "                 I               I                 ",
        "                  H             H                  ",
        "                   G           G                   ",
        "                    F         F                    ",
        "                     E       E                     ",
        "                      D     D                      ",
        "                       C   C                       ",
        "                        B B                        ",
        "                         A                         ",
    ] == Diamond("Z").make_diamond()
