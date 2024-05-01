class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:
            if char == ']':
                temp = ''
                while stack and stack[-1] != '[':
                    temp += stack.pop()
                
                stack.pop() # Remove '['
                
                n = ''
                while stack and not(stack[-1] >= 'a' and stack[-1] <= 'z'):
                    n += stack.pop()

                temp = temp[::-1]
                n = int(n[::-1])

                while n > 0:
                    stack.append(temp)
                    n -= 1
            else:
                stack.append(char)
        
        result = ''.join(stack)
        
        return result 



        