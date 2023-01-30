class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt1 = Counter(self.nums1)
        self.cnt2 = Counter(self.nums2)
        

    def add(self, index: int, val: int) -> None:
        self.cnt2[self.nums2[index]] -= 1
        self.cnt2[self.nums2[index] + val] = self.cnt2.get(self.nums2[index] + val, 0) + 1
        self.nums2[index] += val
        
        

    def count(self, tot: int) -> int:
        res = 0
        for key, val in self.cnt1.items():
            if tot - key in self.cnt2.keys():
                res += val * self.cnt2[tot-key]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)