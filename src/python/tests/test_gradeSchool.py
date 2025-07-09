from weekly_exercises.gradeSchool import GradeSchool


def test_roster_is_empty_when_no_student_is_added() -> None:
    school = GradeSchool()

    assert [] == school.Roster()


def test_add_a_student() -> None:
    school = GradeSchool()

    school.AddStudent(name="Aimee", grade=2)

    assert [True] == school.Added()


def test_student_is_added_to_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Aimee", grade=2)

    assert ["Aimee"] == school.Roster()


def test_adding_multiple_students_in_the_same_grade_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="Paul", grade=2)

    assert [True, True, True] == school.Added()


def test_multiple_students_in_the_same_grade_are_added_to_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.Roster()


def test_cannot_AddStudent_to_same_grade_in_the_roster_more_than_once() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="Paul", grade=2)

    assert [True, True, False, True] == school.Added()


def test_student_not_added_to_same_grade_in_the_roster_more_than_once() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.Roster()


def test_adding_students_in_multiple_grades() -> None:
    school = GradeSchool()

    school.AddStudent(name="Chelsea", grade=3)
    school.AddStudent(name="Logan", grade=7)

    assert [True, True] == school.Added()


def test_students_in_multiple_grades_are_added_to_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Chelsea", grade=3)
    school.AddStudent(name="Logan", grade=7)

    assert ["Chelsea", "Logan"] == school.Roster()


def test_cannot_add_same_student_to_multiple_grades_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=3)
    school.AddStudent(name="Paul", grade=3)

    assert [True, True, False, True] == school.Added()


def test_student_not_added_to_multiple_grades_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=3)
    school.AddStudent(name="Paul", grade=3)

    assert ["Blair", "James", "Paul"] == school.Roster()


def test_students_are_sorted_by_grades_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Jim", grade=3)
    school.AddStudent(name="Peter", grade=2)
    school.AddStudent(name="Anna", grade=1)

    assert ["Anna", "Peter", "Jim"] == school.Roster()


def test_students_are_sorted_by_name_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Peter", grade=2)
    school.AddStudent(name="Zoe", grade=2)
    school.AddStudent(name="Alex", grade=2)

    assert ["Alex", "Peter", "Zoe"] == school.Roster()


def test_students_are_sorted_by_grades_and_then_by_name_in_the_roster() -> None:
    school = GradeSchool()

    school.AddStudent(name="Peter", grade=2)
    school.AddStudent(name="Anna", grade=1)
    school.AddStudent(name="Barb", grade=1)
    school.AddStudent(name="Zoe", grade=2)
    school.AddStudent(name="Alex", grade=2)
    school.AddStudent(name="Jim", grade=3)
    school.AddStudent(name="Charlie", grade=1)

    assert ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"] == school.Roster()


def test_grade_is_empty_if_no_students_in_the_roster() -> None:
    school = GradeSchool()

    assert [] == school.Grade(1)


def test_grade_is_empty_if_no_students_in_that_grade() -> None:
    school = GradeSchool()

    school.AddStudent(name="Peter", grade=2)
    school.AddStudent(name="Zoe", grade=2)
    school.AddStudent(name="Alex", grade=2)
    school.AddStudent(name="Jim", grade=3)

    assert [] == school.Grade(1)


def test_student_not_added_to_same_grade_more_than_once() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="Paul", grade=2)

    assert ["Blair", "James", "Paul"] == school.Grade(2)


def test_student_not_added_to_multiple_grades() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=3)
    school.AddStudent(name="Paul", grade=3)

    assert ["Blair", "James"] == school.Grade(2)


def test_student_not_added_to_other_grade_for_multiple_grades() -> None:
    school = GradeSchool()

    school.AddStudent(name="Blair", grade=2)
    school.AddStudent(name="James", grade=2)
    school.AddStudent(name="James", grade=3)
    school.AddStudent(name="Paul", grade=3)

    assert ["Paul"] == school.Grade(3)


def test_students_are_sorted_by_name_in_a_grade() -> None:
    school = GradeSchool()

    school.AddStudent(name="Franklin", grade=5)
    school.AddStudent(name="Bradley", grade=5)
    school.AddStudent(name="Jeff", grade=1)

    assert ["Bradley", "Franklin"] == school.Grade(5)
