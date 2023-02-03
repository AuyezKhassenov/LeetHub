class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        words = text.split()
        prev_minus2, prev_minus1 = words.pop(0), words.pop(0)
        for word in words:
            if prev_minus2 == first and prev_minus1 == second:
                res.append(word)
            prev_minus2, prev_minus1 = prev_minus1, word
            
        return res
            