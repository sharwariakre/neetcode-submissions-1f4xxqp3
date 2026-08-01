class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.minutes = 0
        q = deque()


        def bfs():
            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            while q:
                rotten = False
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        if ((row+dr) in range(rows) and 
                        (col+dc) in range(cols) and (row+dr, col+dc) not in visited
                        and grid[row+dr][col+dc] == 1):
                            rotten = True
                            visited.add((row+dr, col+dc))
                            grid[row+dr][col+dc] = 2
                            q.append((row+dr, col+dc))
                if rotten:
                    self.minutes += 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
        bfs()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return self.minutes