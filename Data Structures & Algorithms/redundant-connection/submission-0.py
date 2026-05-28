class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {}


        def dfs(s,t,visited):
            if s == t:
                return True
            visited.add(s)

            for nei in graph[s]:
                if nei not in visited:
                    if dfs(nei,t,visited):
                        return True
            return False



        for u,v in edges:

            if u not in graph:
                graph[u] = []

            if v not in graph:
                graph[v] = []
            
            visited = set()

            if graph[u] and graph[v]:
                if dfs(u,v,visited):
                    return [u,v]
            
            graph[u].append(v)
            graph[v].append(u)

        



        