class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return [s.split().index(i) for i in s.split()] == [pattern.find(i) for i in pattern]
        