class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
     
        i = 0
        multiplier = len(digits) - 1
        digit = 0
        while (i < len(digits)):
            digit += (digits[i] * (10**multiplier))
            i += 1
            multiplier -= 1
        
        digit += 1
        result = []
        for num in str(digit):
            result.append(int(num))
        
        return result
       

        