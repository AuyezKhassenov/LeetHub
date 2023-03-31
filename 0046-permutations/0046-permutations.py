class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i, perm, nums):
            if i >= n:
                res.append(perm)
                return
            for j in range(len(nums)):
                dfs(i+1, perm + [nums[j]], nums[:j] + nums[j+1:])
            
        dfs(0, [], nums)
        
        return res