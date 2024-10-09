class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for br in s:
            if br == '(':
                stack.append(br)
            else:    
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(br)
            
        return len(stack)