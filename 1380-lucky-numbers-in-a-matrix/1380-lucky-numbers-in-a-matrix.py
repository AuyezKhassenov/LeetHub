class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i, row in enumerate(matrix):
            elem = float('infinity')
            for j, col in enumerate(row):
                if col < elem:
                    elem = col
                    index = j
            if all(elem >= matrix[k][index] for k in range(len(matrix))):
                res.append(elem)
        return res
                
        