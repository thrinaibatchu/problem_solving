class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build an adjancyList
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        visited = [0 for _ in range(n)]

        #BFS
        def bfs(source):
            q = deque([source])
            visited[source] = 1

            while q:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == 0:
                        visited[neighbor] =1
                        q.append(neighbor)

        #dfs
        def dfs(node):
            visited[node] = 1
            for neighbor in adjList[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor)
        
        #count connected components by calling bfs/dfs multiple times.
        connected = 0
        for v in range(n):
            if visited[v] == 0:
                connected+=1
                bfs(v)
        
        return connected