class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = []
            for i in range(len(nums)//2):
                if not i%2:
                    temp.append(min(nums[2*i], nums[2*i+1]))
                else:
                    temp.append(max(nums[2*i], nums[2*i+1]))
            print(temp)
            nums = temp.copy()
            print(nums)
        return nums[0]
                
                
        