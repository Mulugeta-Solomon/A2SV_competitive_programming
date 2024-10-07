class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        lookUp = {'AB', 'CD'}

        for let in s:
            if stack and (stack[-1] + let) in lookUp: 
                stack.pop()
                continue
            stack.append(let)
 
        return len(stack) 

                