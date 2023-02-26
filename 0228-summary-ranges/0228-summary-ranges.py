class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) > 0:
            start = nums[0]
            end = nums[0]
            for i, num in enumerate(nums): 
                if i < (len(nums) - 1):
                    next = nums[i+1]
                if i < (len(nums) - 1) and nums[i+1] == num + 1:
                    end = next  
                    continue
                if i < (len(nums) - 1) and start != end:
                    res.append(str(start)+"->"+str(end))
                    start = next
                    end = next
                elif i < (len(nums) - 1) and start == end:
                    res.append(str(start))
                    start = next
                    end = next
                if i+1 == len(nums) and start != end:
                    res.append(str(start)+"->"+str(end))
                elif i+1 == len(nums) and start == end:
                    res.append(str(start))
            return res
        else:
            return []

        