class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left, right, result = [-1] * 26, [-1] * 26, 0

        for i, char in enumerate(s):
            curr = ord(char) - ord('a')
            if left[curr] == -1:
                left[curr] = i
            right[curr] = i
        
        for i in range(26):
            if left[i] != -1:
                curr = set()
                for k in range(left[i] + 1, right[i]):
                    curr.add(s[k])        
                result += len(curr)

        return result