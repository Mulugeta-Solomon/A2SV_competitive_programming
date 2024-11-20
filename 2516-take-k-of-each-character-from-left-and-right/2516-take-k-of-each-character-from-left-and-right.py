class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count, left, right = [0] * 3, 0, 0

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        if min(count) < k:
            return -1

        while right < len(s):
            count[ord(s[right]) - ord('a')] -= 1

            if min(count) < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1

            right += 1

        return len(s) - (right - left)


        