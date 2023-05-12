class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        exists = False
        for i in range(h-n+1):
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    exists = True
                else:
                    exists = False
                    break
            if exists:
                return i
        return -1
            
        