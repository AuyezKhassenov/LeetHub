class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]
        
        out = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    out += 1
                    
        return out
                    
        