class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            m = l + (r - l) // 2
            cnt_days = self.count_ships(m, weights, days) 
            if cnt_days > days:
                l = m + 1
            elif cnt_days <= days:
                r = m
                
        return r
            
            
    def count_ships(self, capacity, weights, days):
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
            if cnt_ship > days:
                break
        return cnt_ship + (tmp_w != 0) 
            
        
                