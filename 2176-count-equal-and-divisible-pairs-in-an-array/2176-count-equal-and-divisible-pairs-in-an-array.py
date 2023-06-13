class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mem = defaultdict(list)
        for i, num in enumerate(nums):
            mem[num].append(i)
            
        res = 0
        
        for val in mem.values():
            n = len(val)
            if n >= 2:
                for i, num in enumerate(val):
                    for j in range(i+1, n):
                        if not num*val[j]%k:
                            res += 1
        return res