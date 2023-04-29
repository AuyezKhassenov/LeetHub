class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        table = str.maketrans('abcdefghij', '0123456789')
        return int(firstWord.translate(table)) + int(secondWord.translate(table)) == int(targetWord.translate(table))
        