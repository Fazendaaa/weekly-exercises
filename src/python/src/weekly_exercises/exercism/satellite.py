# Satellite
#
# Imagine you need to transmit a binary tree to a satellite approaching Alpha
# Centauri and you have limited bandwidth. Since the tree has no repeating items
# it can be uniquely represented by its pre-order and in-order traversals.
#
# Write the software for the satellite to rebuild the tree from the traversals.
#
# A pre-order traversal reads the value of the current node before (hence "pre")
# reading the left subtree in pre-order. Afterwards the right subtree is read in
# pre-order.
#
# An in-order traversal reads the left subtree in-order then the current node
# and finally the right subtree in-order. So in order from left to right.
#
# For example the pre-order traversal of this tree is [a, i, x, f, r]. The
# in-order traversal of this tree is [i, a, f, x, r]
#
#      a
#     / \
#    i   x
#       / \
#      f   r
#
# Note: the first item in the pre-order traversal is always the root.
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
# a ValueError if the preorder and inorder arguments are mis-matched
# length-wise, element-wise, or the elements are not unique. The tests will only
# pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
#   # if preorder and inorder are not the same length
#   raise ValueError("traversals must have the same length")
#
#   # if preorder and inorder do not share the same elements
#   raise ValueError("traversals must have the same elements")
#
#   # if element repeat (are not unique)
#   raise ValueError("traversals must contain unique items")
#
# Reference:
#   - https://exercism.org/tracks/python/exercises/satellite
#

from __future__ import annotations

from typing import Optional, TypedDict


class Traversals(TypedDict):
    value: Optional[str]
    left: "Optional[Traversals | dict[None, None]]"
    right: "Optional[Traversals | dict[None, None]]"


def treeFromTraversals(
    preorder: list[str],
    inorder: list[str],
) -> Traversals:
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    if not preorder or not inorder:
        return {}

    root = preorder[0]
    rootIndex = inorder.index(root)
    leftInorder = inorder[:rootIndex]
    rightInorder = inorder[rootIndex + 1 :]
    leftPreorder = preorder[1 : len(leftInorder) + 1]
    rightPreorder = preorder[len(leftInorder) + 1 :]

    return {
        "value": root,
        "left": treeFromTraversals(leftPreorder, leftInorder),
        "right": treeFromTraversals(rightPreorder, rightInorder),
    }
