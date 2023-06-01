class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        amount.sort(reverse=True)
        while amount[0] != 0:
            if amount[1] == 0:
                return res + amount[0]
            else:
                amount[0] -= 1
                amount[1] -= 1
                res += 1
            amount.sort(reverse=True)
        return res