class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        curr, target = bin(num1).count('1'), bin(num2).count('1')
        result = num1

        for i in range(32):
            if curr > target and (1 << i) & num1 > 0:
                result = result ^ (1 << i)
                curr -= 1
            if curr < target and (1 << i) & num1 == 0:
                result = result ^ (1 << i)
                curr += 1
        
        return result 


