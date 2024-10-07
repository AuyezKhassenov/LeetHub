class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        while l <= r:
            m = (l + r) // 2
            cnt_days = self.count_ships(m, weights) 
            if cnt_days > days:
                l = m + 1
            elif cnt_days <= days:
                ans = m
                r = m - 1
                
        return ans
            
            
    def count_ships(self, capacity, weights):
        cnt_ship = 0
        tmp_w = 0
        n = len(weights)
        i = 0
        while i != n:
            tmp = tmp_w + weights[i]
            if tmp < capacity:
                tmp_w += weights[i]
                i += 1
            elif tmp == capacity:
                cnt_ship += 1
                i += 1
                tmp_w = 0
            else:
                cnt_ship += 1
                tmp_w = 0
        return cnt_ship + (tmp_w != 0) 
            
        
                