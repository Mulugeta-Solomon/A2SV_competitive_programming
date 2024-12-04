class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif ord(str1[i]) == ord('z'):
                if str2[j] == 'a':
                    i += 1
                    j += 1
                else:
                    i += 1

            elif chr(ord(str1[i]) + 1) == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        if j == len(str2):
            return True
        
        return False 
        
