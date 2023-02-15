class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res
            
        
        