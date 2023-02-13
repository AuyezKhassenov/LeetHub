class Solution:
    def maxArea(self, H: List[int]) -> int:
        res,i,j = 0,0,len(H)-1
        while i < j:
            if H[i] < H[j]:
                area = H[i] * (j-i)
                i += 1
            else:
                area = H[j] * (j-i)
                j -= 1
            if res < area: res = area
        return res