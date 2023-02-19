class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        i = 0
        while num_str[i] == '9' and i < len(num_str) - 1:
            i += 1
            
        return int(num_str.replace(num_str[i], '9')) - int(num_str.replace(num_str[0], '0'))
        