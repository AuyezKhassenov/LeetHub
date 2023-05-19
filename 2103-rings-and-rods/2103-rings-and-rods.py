class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = defaultdict(set)
        
        for i in range(len(rings)//2):
            cnt[rings[2*i+1]].add(rings[2*i])
        
        res = 0
        for u,v in cnt.items():
            if len(v) == 3:
                res += 1
        
        return res
            