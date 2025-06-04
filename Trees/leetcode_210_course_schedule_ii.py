# leetcode_210_course_schedule_ii.py
# LeetCode Problem 210: Course Schedule II
# Link: https://leetcode.com/problems/course-schedule-ii/
# Name: Course Schedule II
# Concept: Directed graph, topological sort (DFS with cycle detection).
# Approach:
#   - Build adjacency list from prerequisites.
#   - Use DFS to detect cycles and build topological order (in reverse post-order).
#   - If a cycle is detected, return empty list. Otherwise, return a valid order.
# Time Complexity: O(V + E), where V = number of courses, E = number of prerequisites.
# Space Complexity: O(V + E), for graph and recursion stack.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adjList[v].append(u)

        visited = [-1 for _ in range(numCourses)]
        dept = [-1 for _ in range(numCourses)]
        timestamp = [0]
        order = []

        def dfs(node):
            visited[node] = 0
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor):
                        return True
                else:
                    if dept[neighbor] == -1:
                        return True
            
            order.append(node)
            dept[node] = timestamp[0]
            timestamp[0]+=1
        
        for v in range(numCourses):
            if visited[v] == -1:
                if dfs(v):
                    return []

        order.reverse()
        return order