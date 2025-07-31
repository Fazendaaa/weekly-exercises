#                               Introduction
#
# You have stumbled upon a group of mathematicians who are also
# singer-songwriters. They have written a song for each of their favorite
# numbers, and, as you can imagine, they have a lot of favorite numbers
# (like 0 or 73 or 6174).
#
# You are curious to hear the song for your favorite number, but with so many
# songs to wade through, finding the right song could take a while.
# Fortunately, they have organized their songs in a playlist sorted by the
# title — which is simply the number that the song is about.
#
# You realize that you can use a binary search algorithm to quickly find a song
# given the title.
#
#   Instructions
#
# Your task is to implement a binary search algorithm.
#
# A binary search algorithm finds an item in a list by repeatedly splitting it
# in half, only keeping the half which contains the item we're looking for.
# It allows us to quickly narrow down the possible locations of our item until
# we find it, or until we've eliminated all possible locations.
#
#   Caution
#
# Binary search only works when a list has been sorted.
#
# The algorithm looks like this:
#
#   - Find the middle element of a sorted list and compare it with the item
#     we're looking for.
#   - If the middle element is our item, then we're done!
#   - If the middle element is greater than our item, we can eliminate that
#     element and all the elements after it.
#   - If the middle element is less than our item, we can eliminate that element
#     and all the elements before it.
#   - If every element of the list has been eliminated then the item is not in
#     the list.
#   - Otherwise, repeat the process on the part of the list that has not been
#     eliminated.
#
# Here's an example:
#
# Let's say we're looking for the number 23 in the following sorted list:
# [4, 8, 12, 16, 23, 28, 32].
#
#   - We start by comparing 23 with the middle element, 16.
#   - Since 23 is greater than 16, we can eliminate the left half of the list,
#     leaving us with [23, 28, 32].
#   - We then compare 23 with the new middle element, 28.
#   - Since 23 is less than 28, we can eliminate the right half of the list:
#     [23].
#   - We've found our item.
#
#   Exception messages
#
# Sometimes it is necessary to raise an exception. When you do this, you should
# always include a meaningful error message to indicate what the source of the
# error is. This makes your code more readable and helps significantly with
# debugging. For situations where you know that the error source will be a
# certain type, you can choose to raise one of the built in error types, but
# should still include a meaningful message.
#
# This particular exercise requires that you use the raise statement to "throw"
# a ValueError when the given value is not found within the array. The tests
# will only pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
# # example when value is not found in the array.
# raise ValueError("value not in array")
#
# Reference:
# - https://exercism.org/tracks/python/exercises/binary-search
# - https://en.wikipedia.org/wiki/Binary_search_algorithm
#


def binarySearch(array: list[int], target: int) -> int:
    """
    Performs a binary search on a sorted list to find the index of a target value.

    Args:
        array (list[int]): The sorted list to search.
        target (int): The value to search for in the list.

    Returns:
        int: The index of the target value in the list.

    Raises:
        ValueError: If the target value is not found in the list.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            low = mid + 1

        if array[mid] > target:
            high = mid - 1

    raise ValueError("value not in array")
