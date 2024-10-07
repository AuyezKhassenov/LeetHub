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
        for w in weights:
            tmp_w += w
            if tmp_w > capacity:
                tmp_w = w
                cnt_ship += 1
            if cnt_ship > days:
                break
        return cnt_ship + (tmp_w != 0) 
            
        
                