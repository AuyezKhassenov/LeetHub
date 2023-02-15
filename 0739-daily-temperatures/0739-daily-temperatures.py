class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append([t,i])
        return res
            
        
        