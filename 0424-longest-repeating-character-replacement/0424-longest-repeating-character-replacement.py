class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        l = 0
        res = 0
        
        for r in range(len(s)):
            cnt[s[r]] += 1
            max_f = max(cnt.values())
            if r - l + 1 - max_f <= k:
                res = max(res, r - l + 1)
            else:
                cnt[s[l]] -= 1
                l += 1
        return res
        