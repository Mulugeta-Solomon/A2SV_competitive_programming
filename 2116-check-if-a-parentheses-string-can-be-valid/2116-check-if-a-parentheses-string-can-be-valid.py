class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
    
        open_count, close_count = 0, 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                open_count += 1
            elif s[i] == ')':
                open_count -= 1
            if open_count < 0:
                return False

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_count += 1
            elif s[i] == '(':
                close_count -= 1
            if close_count < 0:
                return False

        return True 