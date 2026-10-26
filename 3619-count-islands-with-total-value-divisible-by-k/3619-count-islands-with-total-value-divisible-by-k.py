class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows,cols = len(grid),len(grid[0])
        count = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            value = grid[r][c]
            grid[r][c] = 0

            value += dfs(r+1,c)
            value += dfs(r-1,c)
            value += dfs(r,c+1)
            value += dfs(r,c-1)

            return value
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    total = dfs(i,j)
                    if total % k == 0:
                        count += 1
        return count