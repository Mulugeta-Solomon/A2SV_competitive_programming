class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def recur(num):
            if num <= 0:
                return False
            if num == 1:
                return True
            
            return num % 2 == 0 and recur(num // 2)
        
        return recur(n)