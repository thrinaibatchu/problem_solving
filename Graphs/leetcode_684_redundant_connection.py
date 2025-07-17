# LeetCode 684: Redundant Connection
# https://leetcode.com/problems/redundant-connection/
#
# ✅ Problem:
# Given a graph that started as a tree with one extra edge added, return the redundant edge that creates a cycle.
#
# ✅ Concept:
# Union-Find (Disjoint Set Union), Cycle Detection, Path Compression, Weighted Quick Union
#
# ✅ Approach:
# - Initialize parent and size arrays for Union-Find
# - For each edge, check if both nodes already have the same root (i.e., a cycle exists)
# - If not, union the nodes using size-based merge and path compression
# - Return the edge that first causes a cycle
#
# 🕒 Time Complexity: O(N * α(N)) ~ O(N), where α(N) is the inverse Ackermann function (very slow-growing)
# 🛑 Space Complexity: O(N) for parent and size arrays

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1 for _ in range(len(edges) + 1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            rootu = find(u)
            rootv = find(v)
            if rootu != rootv:
                if size[rootu] < size[rootv]:
                    parent[rootu] = rootv
                    size[rootv] += size[rootu]
                else:
                    parent[rootv] = rootu
                    size[rootu] += size[rootv]
            else:
                return [u, v]
