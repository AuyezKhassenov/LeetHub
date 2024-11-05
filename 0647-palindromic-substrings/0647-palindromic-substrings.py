class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        n = len(s)
        
        def dfs(i, step, j):
            if (i - step < 0 or j + step > n - 1) or (s[i - step] != s[j + step]):
                return
            self.ans += 1
            dfs(i, step+1, j)
        
        for i in range(n):
            dfs(i, 0, i)
            if i != n-1:
                dfs(i, 0, i+1)
        return self.ans
                