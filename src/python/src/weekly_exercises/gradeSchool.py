#                               Instructions
#
# Given students' names along with the grade they are in, create a roster
# for the school.
#
# In the end, you should be able to:
#
#   - Add a student's name to the roster for a grade:
#       - "Add Jim to grade 2."
#       - "OK."
#   - Get a list of all students enrolled in a grade:
#       - "Which students are in grade 2?"
#       - "We've only got Jim right now."
#   - Get a sorted list of all students in all grades. Grades should be sorted
#     as 1, 2, 3, etc., and students within a grade should be sorted
#     alphabetically by name.
#       - "Who is enrolled in school right now?"
#       - "Let me think. We have Anna, Barb, and Charlie in grade 1, Alex,
#         Peter, and Zoe in grade 2, and Jim in grade 5. So the answer is: Anna,
#         Barb, Charlie, Alex, Peter, Zoe, and Jim."
#
# Note that all our students only have one name (it's a small town, what do you
# want?), and each student cannot be added more than once to a grade or the
# roster. If a test attempts to add the same student more than once, your
# implementation should indicate that this is incorrect.
#
# The tests for this exercise expect your school roster will be implemented via
# a School class in Python. If you are unfamiliar with classes in Python,
# classes from the Python docs is a good place to start.
#
# Reference
#   - https://exercism.org/tracks/python/exercises/grade-school
#


from bisect import insort
from functools import reduce


class GradeSchool:
    """A class representing a school roster system.

    This class manages student enrollment by grade level, allowing addition of
    students and retrieval of class rosters.
    """

    def __init__(self) -> None:
        """Initialize an empty grade school roster.

        Creates empty dictionaries and lists to track students by grade and
        addition status.
        """
        self.__grades__: dict[int, list[str]] = {}
        self.__added__: list[bool] = []

    def __repr__(self) -> str:
        """Return string representation of the GradeSchool object.

        Returns:
            str: String showing the grades dictionary content
        """
        return f"GradeSchool(grades={self.__grades__})"

    def AddStudent(self, name: str, grade: int) -> None:
        """Add a student to a specific grade.

        Args:
            name (str): Name of the student to add
            grade (int): Grade level to add the student to

        The student will only be added if they are not already enrolled in any
        grade.
        Records the success/failure of the addition attempt.
        """
        self.__grades__.setdefault(grade, [])

        if name not in set(self.Roster()):
            insort(self.__grades__[grade], name)
            self.__added__.append(True)
        else:
            self.__added__.append(False)

    def Grade(self, grade: int) -> list[str]:
        """Get list of students in a specific grade.

        Args:
            grade (int): Grade level to query

        Returns:
            list[str]: List of student names in the specified grade, or empty
                       list if grade doesn't exist
        """
        return self.__grades__[grade] if grade in self.__grades__ else []

    def Added(self) -> list[bool]:
        """Get and clear the list of addition attempt results.

        Returns:
            list[bool]: List of boolean values indicating success/failure of
                        recent addition attempts
        """
        added = self.__added__
        self.__added__ = []

        return added

    def Roster(self) -> list[str]:
        """Get a sorted list of all enrolled students.

        Returns:
            list[str]: List of all student names, sorted by grade and then
                       alphabetically within each grade
        """
        return (
            reduce(
                lambda acc, cur: acc + cur,
                [self.__grades__[index] for index in sorted(self.__grades__.keys())],
            )
            if self.__grades__
            else []
        )
