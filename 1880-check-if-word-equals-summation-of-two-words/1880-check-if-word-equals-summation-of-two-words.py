class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.convert(firstWord) + self.convert(secondWord) == self.convert(targetWord)
        
    def convert(self, s: str) -> int:
        return int("".join([str((ord(char) - ord('a'))) for char in s]))
        