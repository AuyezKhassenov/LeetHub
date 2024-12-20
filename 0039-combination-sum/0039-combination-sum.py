class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(i, cur_sum, cur_list):
            if cur_sum == target:
                ans.append(cur_list[::])
                return
            elif i >= len(candidates) or cur_sum > target:
                return
            cur_list.append(candidates[i])
            dfs(i, cur_sum + candidates[i], cur_list)
            cur_list.pop()
            dfs(i+1, cur_sum, cur_list)
        
        dfs(0, 0, [])
        return ans
                