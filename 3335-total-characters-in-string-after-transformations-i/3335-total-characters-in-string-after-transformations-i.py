class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        for char in s:
            freq[ord(char)- ord('a')] += 1

        while t > 0:
            curr = [0] * 26
            for i in range(len(freq)):
                if i < len(freq) - 1:
                    curr[i + 1] += freq[i] % MOD 
                    freq[i] = 0
                else:
                    curr[0] += freq[i] % MOD
                    curr[1] += freq[i]% MOD
                    freq[i] = 0
            t -= 1
            freq = curr
        return sum(freq) % MOD
        
