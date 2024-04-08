class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        prefix_sum, ptr = [0] * (len(shifts) + 1), 1

        for i in range(len(shifts)-1, -1, -1):
            prefix_sum[ptr] = prefix_sum[ptr-1] + shifts[i]
            ptr += 1
        
        rev_prefix_sum = prefix_sum[::-1]
        result = ''
        for i in range(len(rev_prefix_sum) - 1):
             result += chr(ord(s[i]) + rev_prefix_sum[i])
        
        return result