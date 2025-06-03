# leetcode_909_snakes_and_ladders.py
# LeetCode Problem 909: Snakes and Ladders
# Link: https://leetcode.com/problems/snakes-and-ladders/
# Name: Snakes and Ladders
# Concept: BFS for shortest path in a board game (flattened 2D to 1D mapping).
# Approach:
#   - Flatten 2D board to 1D list in zig-zag order.
#   - BFS from square 1, rolling dice 1-6 for each move.
#   - Use snakes/ladders by jumping to destination when present.
#   - Mark visited squares and count moves.
# Time Complexity: O(n^2), n = board side length.
# Space Complexity: O(n^2), for queue and visited array.

from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        count = 1
        boardList = [0 for _ in range(n * n + 1)]
        zig_zag = 0
        visited = [-1 for _ in range(len(boardList))]

        # Flatten the board into a 1D list in zig-zag order
        for r in range(n - 1, -1, -1):
            if zig_zag == 0:
                for c in range(n):
                    boardList[count] = board[r][c]
                    count += 1
                zig_zag = 1
            else:
                for c in range(n - 1, -1, -1):
                    boardList[count] = board[r][c]
                    count += 1
                zig_zag = 0

        def bfs(source):
            q = deque([source])
            visited[source] = 0
            while q:
                curr = q.popleft()
                for i in range(1, 7):
                    nxt = curr + i
                    if nxt > n * n:
                        continue
                    # If there's a snake or ladder, jump!
                    if boardList[nxt] != -1:
                        nxt = boardList[nxt]
                    if visited[nxt] == -1:
                        q.append(nxt)
                        visited[nxt] = visited[curr] + 1
                        if nxt == n * n:
                            return visited[nxt]
            return -1
        
        return bfs(1)
