class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        source = image[sr][sc]
        if source == color:
            return image
        image[sr][sc] = color

        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q.append((sr,sc))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                if ((row+dr) in range(rows) and (col+dc) in range(cols) and image[row+dr][col+dc] == source):
                    q.append((row+dr, col+dc))
                    image[row+dr][col+dc] = color
        return image