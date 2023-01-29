class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        for i, num in enumerate(num):
            if int(num) != cnt[str(i)]:
                return False
        return True
        
        