class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def bt(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            elif total > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            bt(i+1, subset, total + candidates[i])
            
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            bt(i+1, subset, total)
        
        bt(0, [], 0)
        return res
            