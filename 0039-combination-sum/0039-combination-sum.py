class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        
        def dfs(i, combination, total):

            if sum(combination) == target:
                res.append(combination.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            combination.append(candidates[i])
            dfs(i, combination, total + candidates[i])
            
            combination.pop()
            dfs(i+1, combination, total)
        
        dfs(0, [], 0)
        
        return res