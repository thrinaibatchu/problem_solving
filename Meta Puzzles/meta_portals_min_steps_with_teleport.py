"""
Meta Puzzle - Portals
--------------------------------
Problem: You are in an R x C grid where each cell can be empty '.', a wall '#', the start 'S', an exit 'E', or a portal 'a'-'z'. You may move in four directions (up/down/left/right) or teleport instantly between cells with the same portal letter. Determine the minimum number of seconds to reach any exit or return -1 if unreachable.

Link: Internal Meta problem, similar to LeetCode-style grid + BFS + teleport logic.

Concepts: Grid traversal, BFS, shortest path, portals, graph with special edges.

Approach:
- Use BFS to guarantee shortest path.
- Track visited cells using a 2D matrix.
- Preprocess portal positions into a hashmap for O(1) teleport access.
- Use a set to ensure portals are only used once.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

from typing import List
from collections import defaultdict, deque

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    def getNeighbors(r, c):
        neighbors = []
        if r > 0 and G[r-1][c] != '#':
            neighbors.append((r-1, c))
        if c > 0 and G[r][c-1] != '#':
            neighbors.append((r, c-1))
        if r < R - 1 and G[r+1][c] != '#':
            neighbors.append((r+1, c))
        if c < C - 1 and G[r][c+1] != '#':
            neighbors.append((r, c+1))
        return neighbors

    def bfs(r, c):  
        q = deque()
        q.append((r, c, 0))
        visited = [[False for _ in range(C)] for _ in range(R)]
        visited[r][c] = True
        used_portals = set()
        
        while q:
            r, c, time = q.popleft()
            ch = G[r][c]
            if ch == "E":
                return time
            neighbors = getNeighbors(r, c)
            if "a" <= ch <= "z" and ch not in used_portals:
                for nr, nc in portals[ch]:
                    if not visited[nr][nc]:
                        q.append((nr, nc, time+1))
                        visited[nr][nc] = True
                used_portals.add(ch)
            for nr, nc in neighbors:
                if not visited[nr][nc]:
                    q.append((nr, nc, time+1))
                    visited[nr][nc] = True
        return -1  

    s_loc = ()
    portals = defaultdict(list)
    
    for r in range(R):
        for c in range(C):
            ch = G[r][c]
            if ch == "S":
                s_loc = (r, c)
            elif "a" <= ch <= "z":
                portals[ch].append((r, c))

    return bfs(s_loc[0], s_loc[1])
