class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        dp = [0] * (len(sequence) + 1)
        
        for i in range(len(sequence) - 1, -1, -1):
            if (i + len(word) <= len(sequence)) and word == sequence[i: i+len(word)]:
                dp[i] = dp[i + len(word)] + 1
            
        return max(dp)