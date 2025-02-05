class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        freq_s1, freq_s2, diff = [0] * 26, [0] * 26, 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff > 2:
                    return False
                freq_s1[ord(s1[i]) - ord('a')] += 1
                freq_s2[ord(s2[i]) - ord('a')] += 1
        
        return freq_s1 == freq_s2
