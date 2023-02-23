class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
       
        while True:
            if i == len(nums1):
                res += nums2[j:]
                break
            if j == len(nums2):
                res += nums1[i:]
                break
            else:
                if nums1[i][0] == nums2[j][0]:
                    res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    i += 1
                    j += 1
                elif nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
        
        return res
            
            