from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = dict(Counter(nums))
        return max(dict_, key= lambda x: dict_[x])
        
        