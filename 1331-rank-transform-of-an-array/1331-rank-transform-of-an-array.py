class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return 
        distinct_sorted = sorted(list(set(arr)))
        dic = {}
        for i, num in enumerate(distinct_sorted):
            dic[num] = i+1
        res = []
        for num in arr:
            res.append(dic[num])
        return res