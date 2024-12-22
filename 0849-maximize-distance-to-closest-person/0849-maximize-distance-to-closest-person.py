class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left2right = [0 for _ in range(len(seats))]
        right2left = [0 for _ in range(len(seats))]
        prev = 3e4
        for i in range(len(seats)):
            if seats[i] == 1:
                left2right[i] = i
                prev = i
            else:
                left2right[i] = prev
                
        prev = 3e4
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                right2left[i] = i
                prev = i
            else:
                right2left[i] = prev
        print(left2right)
        print(right2left)
        ans = 0
        for i, seat in enumerate(seats):
            if seat == 0:
                ans = max(ans, min(abs(i-left2right[i]), right2left[i]-i))
        return ans
                
        
                
        