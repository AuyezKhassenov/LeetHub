class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        res = 0
        min_num = int(num_str.replace(num_str[0], '0'))
        for num in set(num_str):
            res = max(res, int(num_str.replace(num, '9')) - min_num)
        return res
        