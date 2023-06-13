class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for num in range(1, n+1):
            if num > 9:
                sum_digits = sum([int(char) for char in str(num)])
                groups[sum_digits] += 1
            else:
                groups[num] += 1
        
        max_len = max(groups.values())
        
        return sum(1 for i in groups.values() if i >= max_len)
            
            