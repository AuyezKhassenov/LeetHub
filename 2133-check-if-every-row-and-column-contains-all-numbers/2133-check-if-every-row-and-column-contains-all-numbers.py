class Solution:
    def checkValid(self, mat: List[List[int]]) -> bool:
        return all(len(set(x)) == len(mat) for x in mat + list(zip(*mat)))
        