class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1,1])
            else:
                res = [1]
                for j in range(i-1):
                    res.append(ans[-1][j] + ans[-1][j+1])
                res.append(1)
                ans.append(res)
        return ans
        