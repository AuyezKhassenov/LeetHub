class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        grid = [elem for row in grid for elem in row]
        k = k % len(grid)
        res = grid[-k:] + grid[:-k]
        return [res[i*n:(i+1)*n] for i in range(m)]
        