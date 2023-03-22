class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:return word
        for i, char in enumerate(word):
            if char == ch:
                break
        return word[:i+1][::-1] + word[i+1:]
            
            
        