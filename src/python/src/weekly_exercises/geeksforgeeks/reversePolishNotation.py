# Evaluate the Value of an Arithmetic Expression in Reverse Polish Notation in
# Python
#
# Reverse Polish 'Notation is postfix notation which in terms of mathematical
# notion signifies operators following operands. Let's take a problem statement
# to implement RPN
#
# Problem Statement: The task is to find the value of the arithmetic expression
# present in the array using valid operators like +, -, *, /. Each operand may
# be an integer or another expression.
#
# Note:
#
# The division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero operation.
# Layman Working of RPN as shown
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
# Approach:
#
# The basic approach for the problem is using the stack.
#
# Accessing all elements in the array, if the element is not matching with the
# special character ('+', '-','*', '/') then push the element to the stack.
# Then whenever the special character is found then pop the first two-element
# from the stack and perform the action and then push the element to stack
# again.
# Repeat the above two process to all elements in the array
# At last pop the element from the stack and print the Result
#
# Reference:
#   - https://www.geeksforgeeks.org/python/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-python/
#


from math import trunc
from typing import Callable


class ReversePolishNotation:
    """
    A class to evaluate arithmetic expressions in Reverse Polish Notation (RPN).

    Reverse Polish Notation is a postfix notation where operators follow their operands.
    This class provides functionality to evaluate RPN expressions containing basic arithmetic
    operations (+, -, *, /).
    """

    def __init__(self) -> None:
        """Initialize a new ReversePolishNotation instance."""
        pass

    @classmethod
    def eval(
        cls,
        tokens: list[str],
    ) -> int:
        """
        Evaluate an arithmetic expression in Reverse Polish Notation.

        Args:
            tokens (list[str]): A list of strings representing the RPN expression.
                              Valid tokens include numbers and operators (+, -, *, /).

        Returns:
            int: The result of evaluating the RPN expression.

        Examples:
            >>> ReversePolishNotation.eval(["2", "1", "+", "3", "*"])
            9
            >>> ReversePolishNotation.eval(["4", "13", "5", "/", "+"])
            6

        Note:
            - Division between integers is truncated toward zero
            - The input RPN expression must be valid (will always evaluate to a result)
            - There must not be any divide by zero operations
        """
        operators: dict[str, Callable[[int, int], int]] = {
            "+": lambda first, second: first + second,
            "-": lambda first, second: first - second,
            "*": lambda first, second: first * second,
            "/": lambda first, second: trunc(first / second),
        }
        stack: list[int] = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                secondToLast = stack.pop()
                last = stack.pop()
                stack.append(operators[token](last, secondToLast))

        return stack.pop()
