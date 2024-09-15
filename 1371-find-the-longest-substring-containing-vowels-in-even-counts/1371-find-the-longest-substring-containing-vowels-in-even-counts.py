class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        first_occ = {0: -1}

        mask, result = 0, 0

        for i, letter in enumerate(s):
            if letter in vowels:
                mask ^= (1 << vowels[letter])
            
            if mask in first_occ:
                result = max(result, i - first_occ[mask])
            else:
                first_occ[mask] = i
        
        return result
