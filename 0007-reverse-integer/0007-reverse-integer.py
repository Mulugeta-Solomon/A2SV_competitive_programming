class Solution:
    def reverse(self, x: int) -> int:
    
        flag = False 
        if x < 0:
            flag = True 
            x = abs(x)

        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit 
            x //= 10
        
        if reversed_num < (-2**31) or reversed_num > (2**31 - 1):
            return 0 

        if flag == True:
            return -reversed_num
        
        return reversed_num
        

