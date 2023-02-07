class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
            
        for key,val in cnt.items():
                freq[val].append(key)
        res = []        
        for elem in freq[::-1]:
            for item in elem:
                res.append(item)
            if len(res) == k:
                return res