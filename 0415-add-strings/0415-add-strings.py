class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, result, carry = len(num1) - 1, len(num2) - 1, '', 0

        while i >= 0 and j >= 0:
            curr = carry + int(num1[i]) + int(num2[j])
            result += str(curr % 10)
            carry = curr // 10
            i -= 1
            j -= 1
        
        while i >= 0:
            curr = carry + int(num1[i]) 
            result += str(curr % 10)
            carry = curr // 10
            i -= 1
        
        while j >= 0:
            curr = carry + int(num2[j])
            result += str(curr % 10)
            carry = curr // 10
            j -= 1
        
        if carry:
            result += str(carry)
            
        return result[::-1]