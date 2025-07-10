"""
Problem: Rabbit Hole (Chapter 1) - Meta Puzzle
URL: [Meta Puzzle Portal - Internal Use]  # Replace with actual link if available

Description:
You are navigating an online encyclopedia with N pages (numbered 1 to N). Each page i has
a single outbound link to a different page L[i]. Starting from any page, you may follow the
links or stop browsing at any time. A page only counts once even if visited multiple times.

Your goal is to determine the maximum number of **distinct** pages you can visit in one session,
starting from any page.

Constraints:
- 2 ≤ N ≤ 500,000
- 1 ≤ L[i] ≤ N
- L[i] ≠ i

Example:
Input:  N = 4, L = [4, 1, 2, 1]
Output: 4
Explanation: Starting from page 3 → 2 → 1 → 4 visits all pages.

Approach:
- Model the structure as a functional graph (each node has exactly 1 outgoing edge).
- Traverse from each unvisited node using a DFS-like approach.
- Detect cycles during traversal using path + path_index.
- Assign cycle lengths and propagate length info backward for chain nodes.
- Memoize visited nodes to avoid recomputation.
- Track the global max path length across all components.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    # Normalize to 0-based indexing
    L = [x - 1 for x in L]

    visited = [False] * N
    path_len = [0] * N
    max_path = 0

    def explore(start: int):
        nonlocal max_path
        path = []
        path_index = {}
        node = start

        while True:
            path_index[node] = len(path)
            path.append(node)
            next_node = L[node]

            if next_node in path_index:
                # Cycle detected
                cycle_start_index = path_index[next_node]
                cycle_length = len(path) - cycle_start_index
                max_path = max(max_path, cycle_length)

                # Assign cycle length to cycle nodes
                for i in range(cycle_start_index, len(path)):
                    u = path[i]
                    visited[u] = True
                    path_len[u] = cycle_length

                # Assign path lengths to nodes before the cycle
                for i in range(cycle_start_index - 1, -1, -1):
                    u = path[i]
                    next_u = path[i + 1]
                    visited[u] = True
                    path_len[u] = path_len[next_u] + 1
                    max_path = max(max_path, path_len[u])
                return

            if visited[next_node]:
                # Already computed chain
                known_len = path_len[next_node]
                for i in range(len(path) - 1, -1, -1):
                    u = path[i]
                    visited[u] = True
                    path_len[u] = known_len + 1
                    known_len = path_len[u]
                    max_path = max(max_path, path_len[u])
                return

            node = next_node

    # Explore from all unvisited nodes
    for i in range(N):
        if not visited[i]:
            explore(i)

    return max_path
