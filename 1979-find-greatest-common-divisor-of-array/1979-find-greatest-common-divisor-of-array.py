class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a 
            return gcd(b, a % b)
        
        min_, max_ = min(nums), max(nums)
        
        return gcd(min_, max_)