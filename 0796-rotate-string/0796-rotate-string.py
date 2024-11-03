class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n, i, check = len(s), 0, s

        while True:
            s = s[1:] + s[0]
            if s == goal:
                return True 
            if s == check:
                return False
