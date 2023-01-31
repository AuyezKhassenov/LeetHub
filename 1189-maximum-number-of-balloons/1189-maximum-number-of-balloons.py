class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt_balloon = Counter('balloon')
        cnt_txt = Counter(text)
        res = []
        for key, val in cnt_balloon.items():
            if key in cnt_txt.keys():
                res.append(cnt_txt[key] // val)
            else:
                return 0
        return min(res)
        