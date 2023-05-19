class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = defaultdict(set)
        rings = [rings[i:i+2] for i in range(0,len(rings), 2)]
        [cnt[key].add(value) for value, key in rings]
        res = 0
        for key,val in cnt.items():
            if len(val) == 3:
                res += 1
        return res


            