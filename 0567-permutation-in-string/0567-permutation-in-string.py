class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        freq1, freq2 = Counter(s1), Counter(s2[0:len(s1)])
        if freq1 == freq2:
            return True
        
        left, right = 1, len(s1)

        while right < len(s2):
            freq2[s2[left - 1]] -= 1
            freq2[s2[right]] += 1

            if freq1 == freq2:
                return True
            right += 1
            left += 1
        
        return False