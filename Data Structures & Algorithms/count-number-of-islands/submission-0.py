class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        nr = len(grid)
        nc = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c):
            grid[r][c] = "0"
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < nr and 0 <= new_c < nc and grid[new_r][new_c] == "1":
                    dfs(new_r,new_c)
    
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island_count += 1

        return island_count




