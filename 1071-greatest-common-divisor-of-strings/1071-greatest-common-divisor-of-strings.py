class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ptr1, ptr2, result = 0, 0, ''

        while ptr1 < len(str1) and ptr2 < len(str2):
            if str1[ptr1] == str2[ptr2]:
                result += str1[ptr2] 
            ptr1 += 1
            ptr2 += 1
        
        return ''.join(set(result))