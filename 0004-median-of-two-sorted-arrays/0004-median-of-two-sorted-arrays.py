class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        length = total // 2
        
        
        l, r = 0, n1 - 1
        
        while True:
            i = (l+r)//2
            j = length - i - 2
            
            Aleft = nums1[i] if i >= 0 else float('-infinity')
            Aright = nums1[i+1] if (i+1)<n1 else float('infinity')
            Bleft = nums2[j] if j >= 0 else float('-infinity')
            Bright = nums2[j+1] if (j+1)<n2 else float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft < Bright:
                l = i + 1
            else:
                r = i - 1