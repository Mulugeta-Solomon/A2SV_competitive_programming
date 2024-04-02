class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1 
        look_up = set() # to check for seen elements 
                                                     #rl     
        left, long_substr, count = 0, 0, 0   # abcabcbb
                                            # baca
        for right in range(len(s)):
            if s[right] not in look_up:
                look_up.add(s[right])
                long_substr = max(long_substr, right - left + 1)
            else:
                long_substr = max(long_substr, right - left)

                if right == len(s) - 1:
                    break

                while left <= right and s[left] != s[right]:
                    look_up.remove(s[left])
                    left += 1
                left += 1
            
            if right == len(s) - 1 and long_substr == 0:
                long_substr = max(long_substr, right - left + 1)

        return long_substr
                


            
            


            
