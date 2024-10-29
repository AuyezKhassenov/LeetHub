class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums) / 3
        ans = []
        for k, v in cnt.items():
            if v > n:
                ans.append(k)
        return ans