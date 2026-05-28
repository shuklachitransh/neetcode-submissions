class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        comp = 0
        for i in range(n):
            if not visited[i]:
                comp += 1
                dfs(i)
        return comp

