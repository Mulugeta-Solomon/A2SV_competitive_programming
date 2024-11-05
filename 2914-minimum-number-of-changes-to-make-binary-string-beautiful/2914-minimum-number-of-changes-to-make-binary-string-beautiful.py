class Solution:
    def minChanges(self, s: str) -> int:

        result, i = 0, 0
        while i < len(s):
            if s[i] != s[i + 1]:
                result += 1
            i += 2

        return result



        