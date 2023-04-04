class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def bt(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            elif total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                bt(j+1, subset + [candidates[j]], total + candidates[j])
        
        bt(0, [], 0)
        return res
            