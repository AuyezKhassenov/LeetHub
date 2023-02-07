class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        processed = set()
        for num in nums:
            if num in processed:
                return True
            else:
                processed.add(num)
        return False
        