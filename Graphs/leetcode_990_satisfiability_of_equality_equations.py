# LeetCode 990: Satisfiability of Equality Equations
# https://leetcode.com/problems/satisfiability-of-equality-equations/
#
# ✅ Problem:
# Given a list of equations with variables represented as lowercase letters (a–z),
# determine if it is possible to assign values to variables such that all equations are satisfied.
#
# ✅ Concept:
# Union-Find (Disjoint Set Union), Constraint Satisfaction
#
# ✅ Approach:
# - First pass: union all "==" equations to group equal variables
# - Second pass: check all "!=" equations — if two variables are in the same group, return False
# - Use path compression and union by size to optimize
#
# 🕒 Time Complexity: O(N * α(N)), where α(N) is the inverse Ackermann function
# 🛑 Space Complexity: O(1) since there are only 26 lowercase letters (a–z)

from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        for eq in equations:
            a, b = eq[0], eq[3]
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b

        size = {x: 1 for x in parent}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # First pass: union all variables with "=="
        for eq in equations:
            if eq[1:3] == '==':
                u, v = eq[0], eq[3]
                rootu = find(u)
                rootv = find(v)
                if rootu != rootv:
                    if size[rootu] < size[rootv]:
                        parent[rootu] = rootv
                        size[rootv] += size[rootu]
                    else:
                        parent[rootv] = rootu
                        size[rootu] += size[rootv]

        # Second pass: check all "!=" constraints
        for eq in equations:
            if eq[1:3] == '!=':
                u, v = eq[0], eq[3]
                if find(u) == find(v):
                    return False

        return True
