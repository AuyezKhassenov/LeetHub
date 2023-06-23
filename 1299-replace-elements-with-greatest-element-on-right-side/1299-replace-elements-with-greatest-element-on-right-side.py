class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_res = []
        max_temp = 0
        for num in arr[::-1]:
            max_temp = max(max_temp, num)
            max_res.append(max_temp)
        return max_res[:-1][::-1] + [-1]
            