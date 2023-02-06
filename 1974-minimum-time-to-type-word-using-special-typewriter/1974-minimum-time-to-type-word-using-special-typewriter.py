class Solution:
    def minTimeToType(self, word: str) -> int:
        start = 97
        res = 0
        for w in word:
            distance = abs(ord(w) - start)
            res += min(distance, 26 - distance) + 1
            start = ord(w)
        return res
        