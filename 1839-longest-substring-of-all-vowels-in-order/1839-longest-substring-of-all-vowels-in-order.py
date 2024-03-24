class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        left, max_subarr, seen = 0, 0, defaultdict(int)

        for right in range(len(word)):
            if right > 0 and word[right] < word[right-1]:
                seen = defaultdict(int)
                left = right 

            seen[word[right]] += 1

            if len(seen) == 5:
                max_subarr = max(max_subarr, right - left + 1)
        
        return max_subarr
