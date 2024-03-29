class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            result.append(chr((columnNumber-1)%26+ord('A')))
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)
        