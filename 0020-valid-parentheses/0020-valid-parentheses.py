# class Stack:
#     def __init__(self) -> None:
#         self.stack = []

#     def push(self, char:str):
#         self.stack.append[char]
    
#     def pop(self):
#         if self.stack:
#             return self.stack.pop()
    
#     def peek(self):
#         if self.stack:
#             return self.stack[-1]

#     def isEmpty(self):
#         return len(self.stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        look_up = {')':'(', '}':'{',']':'['}
        
        for i in range(len(s)):
            if i%2 == 0:
                stack.append(s[i])
            else:
                if s[i] not in look_up:
                    return False 
                if stack.pop() != look_up[s[i]]:
                    return False 
                continue 
        
        return len(stack) == 0


        
