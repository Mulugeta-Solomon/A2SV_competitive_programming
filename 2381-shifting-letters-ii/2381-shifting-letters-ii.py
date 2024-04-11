class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix_sum = [0] * (len(s) + 1)

        for i in range(len(shifts)):
            left, right, direction = shifts[i]
            if direction == 0:
                prefix_sum[left] += -1
                prefix_sum[right+1] += 1
            else:
                prefix_sum[left] += 1
                prefix_sum[right+1] += -1
        
        for i in range(len(prefix_sum) - 1):
            prefix_sum[i+1] += prefix_sum[i]  
        
        result = '' 
        for i in range(len(s)):
            result += chr((ord(s[i]) + prefix_sum[i] - 97) % 26 + 97)

        return result  
