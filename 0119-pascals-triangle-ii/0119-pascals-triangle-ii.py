class Solution:
    def getRow(self, rowIndex):

        if rowIndex == 0:
            return [1]
        
        res = [1]
        for i in range(rowIndex):
            res = [1] + [a + b for a,b in zip(res[:-1], res[1:])] + [1]
        
        return res
        
        