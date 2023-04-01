class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        
        def dfs(i, combination):
            if i >= len(candidates):
                return
            if sum(combination) == target:
                res.append(combination.copy())
                return
            elif sum(combination) > target:
                return
            
            combination.append(candidates[i])
            dfs(i, combination)
            
            combination.pop()
            dfs(i+1, combination)
        
        dfs(0, [])
        
        return res