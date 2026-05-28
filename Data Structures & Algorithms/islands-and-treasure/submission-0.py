class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        INF = 2147483647
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            r,c = queue.popleft()

            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr , nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))



