class Solution:
    def sortSentence(self, s: str) -> str:
        words = [[word[:-1], int(word[-1])] for word in s.split()]
        return " ".join(word[0] for word in sorted(words, key=lambda k:k[1]))