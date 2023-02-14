class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','/','*'}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    c = b + a
                elif token == '-':
                    c = b - a
                elif token == '*':
                    c = b * a
                elif token == '/':
                    c = int(b / a)
                stack.append(c)
        return stack[0]
                
                
                
                
            
        