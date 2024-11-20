class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count, left, right, result = [0] * 3, 0, 0, float('inf')

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        if min(count) < k:
            return -1

        while right < len(s):
            count[ord(s[right]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1

            result = min(result, len(s) - (right - left + 1))
            right += 1

        return result


        