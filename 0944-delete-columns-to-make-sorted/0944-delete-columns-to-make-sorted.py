class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
    
        return sum(list(word) != sorted(word) for word in zip(*strs))