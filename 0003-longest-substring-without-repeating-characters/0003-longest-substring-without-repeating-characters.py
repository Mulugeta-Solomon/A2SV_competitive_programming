class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        freq = defaultdict(int)

        for right in range(len(s)):
            while s[right] in freq and left < right:
                freq[s[left]] -= 1
                if not freq[s[left]]:
                    del freq[s[left]]
                left += 1

            freq[s[right]] += 1 
            result = max(result, right - left + 1)

        return result