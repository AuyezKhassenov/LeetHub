class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
            if grid[i][0] < 0:
                res += (m - i)*n
                break
            for j in range(n):
                if grid[i][j] < 0:
                    res += n - j
                    break
        return res
                