#                           Redundant Signal Towers
#
#   Description:
#
# There are N signal towers located on a number line, each tower at position xi
# with an initial strength coefficient ki. At any point x on the number line,
# the signal strength received from tower i is calculated as
# Si(x) = 1 / | x - xi | + ki. It is known that any device on the number line
# will only connect to the tower providing the strongest signal. Now, in order
# to reduce costs, the maintainer wants to shut down some towers. The question
# is: What is the maximum number of towers that can be shut down such that the
# signal strength received by any point on the number line remains unchanged?
#
# We are given that both xi and ki are integers, and they satisfy the following
# constraints:
#
#   - 1 ≤ N^5
#   - 1 ≤ N ≤ 10^9, unique
#   - 1 ≤ ki ≤ 10^9
#
# Using an O(N^2) approach for this problem will lead to a timeout.
#
#   Example
#
# Given 3 towers:
#
#   - x0 = 1, k0 = 1
#   - x1 = 2, k1 = 1
#   - x2 = 4, k2 = 3
#
# For example, calculating the signal strength at x = 5, we have S0(5) = 0.2,
# S1(5) = 0.25, and S2(5) = 0.25. Towers 1 and 2 both provide the strongest
# signal, and the signal received at this point is 0.25.
#
# Tower 0 dominates the signal strength over the range (−∞,1.5], while tower 1
# dominates over [1.5,∞). This means either tower 0 or 1 provides an equal or
# stronger signal than tower 2 at any position. Therefore, tower 2 can be safely
# shut down. The answer in this case should be 1.
#
#   Hints
#
#   - Try to use 1 / Si(x) instead. It's easier and has a lot of nice properties.
#   - It can be proven that Si(xj) ≥ Sj(xj) ⟺ ∀x, Si(x) ≥ Sj(x).
#
# Reference:
# - https://www.codewars.com/kata/67fbdd269bf8d73514187d58
#


class Tower:
    def __init__(
        self,
        position: float,
        strength: float,
    ) -> None:
        self.position = position
        self.strength = strength

    def signal_strength(self, x: float) -> float:
        return 1 / abs(x - self.position) + self.strength


class SignalTowers:
    def __init__(self, combination: list[tuple[float, float]]) -> None:
        self.n = len(combination)
        self.towers = [Tower(item[0], item[1]) for item in combination]

    def is_dominated(self, i: int, j: int) -> bool:
        # Check if tower i is dominated by tower j
        _, _ = self.towers[i].position, self.towers[i].strength
        xj, _ = self.towers[j].position, self.towers[j].strength

        # Using the hint: Si(xj) ≥ Sj(xj) ⟺ ∀x, Si(x) ≥ Sj(x)
        # Compare signal strengths at position xj
        return self.towers[i].signal_strength(xj) <= self.towers[j].signal_strength(xj)

    def find_redundant_towers(self) -> int:
        # Create adjacency matrix for domination relationships
        dominated = [[False] * self.n for _ in range(self.n)]

        # Check domination relationships between all pairs
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    dominated[i][j] = self.is_dominated(i, j)

        # Count towers that are completely dominated by at least one other tower
        redundant = 0
        for i in range(self.n):
            for j in range(self.n):
                if i != j and dominated[i][j]:
                    redundant += 1
                    break

        return redundant
