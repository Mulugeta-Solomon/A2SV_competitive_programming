class Solution:
    def removeStars(self, s: str) -> str:
        Stack = []

        for char in s:
            if char != '*':
                Stack.append(char)
            else:
                Stack.pop()
        
        return ''.join(Stack)