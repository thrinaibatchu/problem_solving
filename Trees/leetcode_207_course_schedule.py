# leetcode_207_course_schedule.py
# LeetCode Problem 207: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/
# Name: Course Schedule
# Concept: Directed graph, cycle detection (DFS with arrival/departure time).
# Approach:
#   - Build the adjacency list from prerequisites.
#   - Use DFS to detect cycles by tracking visited and departure arrays.
#   - If a cycle is found, return False; otherwise, return True.
# Time Complexity: O(V + E), where V = number of courses, E = number of prerequisites.
# Space Complexity: O(V + E), for the graph and recursion stack.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adjList[v].append(u)

        visited = [-1 for _ in range(numCourses)]
        dept = [-1 for _ in range(numCourses)]
        timestamp = [0]

        def dfshasCycle(node):
            visited[node] = 0
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    if dfshasCycle(neighbor):
                        return True
                elif dept[neighbor] == -1:
                    return True
            dept[node] = timestamp[0]
            timestamp[0] += 1
            return False
        
        for v in range(numCourses):
            if visited[v] == -1:
                if dfshasCycle(v):
                    return False
        return True
