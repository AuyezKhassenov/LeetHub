class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = []
        for i, val in enumerate(score):
            heappush(rankings, (-val,i))
        ans = [''] * len(score)
        r = 1
        ranks = ["Gold Medal",'Silver Medal','Bronze Medal']
        while len(rankings) != 0:
            _, i = heappop(rankings)
            if r <= 3:
                ans[i] = ranks[r-1]
            else:
                ans[i] = f'{r}'
            r += 1
        return ans