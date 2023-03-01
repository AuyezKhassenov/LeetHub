class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        r, c = 0, n - 1
        
        while r < m and c >= 0:
            if grid[r][c] < 0:
                res += m - r
                c -= 1
            else:
                r += 1
                
        return res