class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        lookup, result = defaultdict(list), []
        for i, word in enumerate(words):
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            lookup[i] = freq
        
        for idx in range(26):
            curr = float('inf')
            for i, freq in lookup.items():
                if not freq[idx]:
                    curr = 0
                    break
                curr = min(curr, freq[idx])
        

            result.extend([chr(ord('a') + idx)] * curr)

        return result