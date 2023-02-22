class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c == m * n:
            array = [item for sublist in mat for item in sublist]
            res = []
            for i in range(r):
                res.append(array[c*i:c*(i+1)])
            return res
        else:
            return mat
        