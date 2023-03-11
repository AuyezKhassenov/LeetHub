class Solution:
    def maxScore(self, s: str) -> int:
        res, ones, zeros = 0, s.count('1'), 0
        for i in range(0, len(s)-1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            res = max(res, zeros + ones)
                
        return res
        