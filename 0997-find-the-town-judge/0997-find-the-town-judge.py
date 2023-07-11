class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        sum_trust = [0] * (n+1)
        for i, j in trust:
            sum_trust[i] -= 1
            sum_trust[j] += 1
        for i in range(1, n+1):
            if sum_trust[i]==n-1:
                return i
        return -1