#                                       POV
#
#   Instructions
#
# Reparent a tree on a selected node.
#
# A tree is a special type of graph where all nodes are connected but there are
# no cycles. That means, there is exactly one path to get from one node to
# another for any pair of nodes.
#
# This exercise is all about re-orientating a tree to see things from a
# different point of view. For example family trees are usually presented from
# the ancestor's perspective:
#
#         +------0------+
#         |      |      |
#       +-1-+  +-2-+  +-3-+
#       |   |  |   |  |   |
#       4   5  6   7  8   9
#
# But there is no inherent direction in a tree. The same information can be
# presented from the perspective of any other node in the tree, by pulling it up
# to the root and dragging its relationships along with it. So the same tree
# from 6's perspective would look like:
#
#                6
#                |
#          +-----2-----+
#          |           |
#          7     +-----0-----+
#                |           |
#              +-1-+       +-3-+
#              |   |       |   |
#              4   5       8   9
#
# This lets us more simply describe the paths between two nodes. So for example
# the path from 6-9 (which in the first tree goes up to the root and then down
# to a different leaf node) can be seen to follow the path 6-2-0-3-9.
#
# This exercise involves taking an input tree and re-orientating it from the
# point of view of one of the nodes.
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
# multiple ValueErrors if the Tree() class is passed a tree that cannot be
# reoriented, or a path cannot be found between a start node and an end node.
# The tests will only pass if you both raise the expected exception type and
# include the expected message with it.
#
# Please check the tests and their expected results carefully.
#
# Reference:
#   - https://exercism.org/tracks/python/exercises/pov
#

from __future__ import annotations

from typing import Optional


class Tree:
    def __init__(
        self,
        label: str,
        children: "Optional[list[Tree]]" = None,
    ) -> None:
        self.label = label
        self.children = children if children is not None else []

    def __repr__(self) -> str:
        return f"Tree(label={self.label}, children={self.children})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tree):
            return False
        return (
            self.label == other.label
            and len(self.children) == len(other.children)
            and all(c1 == c2 for c1, c2 in zip(self.children, other.children))
        )

    def from_pov(
        self,
        from_node: str,
    ) -> "Tree":
        # Build parent mapping and find all nodes
        parent_map: dict[str, Optional[str]] = {}
        node_map: dict[str, Tree] = {}
        self._build_maps(None, parent_map, node_map)

        if from_node not in node_map:
            raise ValueError("Tree could not be reoriented")

        # Build the new tree using BFS from the target node
        return self._build_new_tree(from_node, parent_map, node_map)

    def path_to(
        self,
        from_node: str,
        to_node: str,
    ) -> list[str]:
        # Build parent mapping and find all nodes
        parent_map: dict[str, Optional[str]] = {}
        node_map: dict[str, Tree] = {}
        self._build_maps(None, parent_map, node_map)

        if from_node not in node_map or to_node not in node_map:
            raise ValueError("No path found")

        # Find path using BFS
        path = self._find_path_bfs(from_node, to_node, parent_map, node_map)
        if not path:
            raise ValueError("No path found")

        return path

    def _build_maps(
        self,
        parent: "Optional[Tree]",
        parent_map: dict[str, Optional[str]],
        node_map: dict[str, Tree],
    ) -> None:
        node_map[self.label] = self
        parent_map[self.label] = parent.label if parent else None

        for child in self.children:
            child._build_maps(self, parent_map, node_map)

    def _build_new_tree(
        self,
        root_label: str,
        parent_map: dict[str, Optional[str]],
        node_map: dict[str, Tree],
    ) -> "Tree":
        # Use BFS to build the tree to avoid recursion depth issues
        from collections import deque

        # Create new nodes without children first
        new_nodes = {}
        for label in node_map:
            new_nodes[label] = Tree(label)

        # Build the tree structure using BFS from the new root
        visited = set()
        queue = deque([root_label])
        visited.add(root_label)

        while queue:
            current_label = queue.popleft()
            current_node = new_nodes[current_label]

            # Add children: original children + parent (except the path we came from)
            original_node = node_map[current_label]

            # Add original children (except those that are parents in the new tree)
            for child in original_node.children:
                if child.label not in visited and child.label != parent_map.get(
                    current_label
                ):
                    current_node.children.append(new_nodes[child.label])
                    queue.append(child.label)
                    visited.add(child.label)

            # Add parent as a child (if exists and not already visited)
            parent_label = parent_map.get(current_label)
            if parent_label and parent_label not in visited:
                current_node.children.append(new_nodes[parent_label])
                queue.append(parent_label)
                visited.add(parent_label)

        return new_nodes[root_label]

    def _find_path_bfs(
        self,
        start: str,
        end: str,
        parent_map: dict[str, Optional[str]],
        node_map: dict[str, Tree],
    ) -> list[str]:
        from collections import deque

        # BFS to find shortest path
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            current_label, path = queue.popleft()

            if current_label == end:
                return path

            current_node = node_map[current_label]

            # Check original children
            for child in current_node.children:
                if child.label not in visited:
                    visited.add(child.label)
                    queue.append((child.label, path + [child.label]))

            # Check parent
            parent_label = parent_map.get(current_label)
            if parent_label and parent_label not in visited:
                visited.add(parent_label)
                queue.append((parent_label, path + [parent_label]))

        return []
