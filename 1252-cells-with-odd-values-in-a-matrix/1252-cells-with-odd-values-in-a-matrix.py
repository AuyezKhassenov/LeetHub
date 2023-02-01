class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        res = 0
        for indice in indices:
            rows[indice[0]] += 1
            cols[indice[1]] += 1
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2:
                    res += 1
        return res
                
        