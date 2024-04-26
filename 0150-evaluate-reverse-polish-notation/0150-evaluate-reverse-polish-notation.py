class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack, result = [], 0
        
        for token in tokens:
            if token == '+':
                val = stack.pop()
                curr = stack.pop() + val
                stack.append(curr)
            elif token ==  '-':
                val = stack.pop()
                curr = stack.pop() - val
                stack.append(curr)
            elif token == '*':
                val = stack.pop()
                curr = stack.pop() * val
                stack.append(curr)
            elif token == '/':
                val = stack.pop()
                curr = stack.pop() / val
                curr = math.ceil(curr) if curr < 0 else math.floor(curr)
                stack.append(curr)
            else:
                stack.append(int(token))
        
        return stack[0] 
        