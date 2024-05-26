class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        nums = []
        operators = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "/": lambda a,b: int(a / b),
            "*": lambda a,b: a * b
        }
        
        for token in tokens:
            if token in operators:
                b = nums.pop()
                a = nums.pop()
                nums.append(operators[token](a,b))
            else:
                nums.append(int(token))
        
        return nums[0]