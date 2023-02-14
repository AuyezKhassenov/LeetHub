class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if stack == []:
                    return False
                else:
                    a = stack.pop()
                    if bracket != brackets[a]:
                        return False
        return stack == []