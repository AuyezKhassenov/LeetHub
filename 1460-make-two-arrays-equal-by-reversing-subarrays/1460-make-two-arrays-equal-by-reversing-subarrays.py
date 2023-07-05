class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt_target, cnt_arr = Counter(target), Counter(arr)
        return cnt_target == cnt_arr