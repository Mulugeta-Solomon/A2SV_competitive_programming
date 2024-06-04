class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stack = []

        def backtrack(start):
            if start == n:
                for i in range(1, len(stack)):
                    if stack[i] - stack[i-1] != -1:
                        return False    
                return len(stack) >= 2

            for i in range(start + 1, n + 1):
                num = int(s[start:i])
                if not stack or num - stack[-1] == -1:
                    stack.append(num)
                    if backtrack(i):
                        return True
                    stack.pop()
            return False
        
        return backtrack(0)
        