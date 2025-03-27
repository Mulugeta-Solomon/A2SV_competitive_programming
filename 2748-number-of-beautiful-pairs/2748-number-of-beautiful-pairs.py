class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            curr = nums[i] % 10
            for j in range(i):
                n = nums[j]
                while n >= 10:
                    n //= 10
                if gcd(curr, n) == 1:
                    result += 1
        
        return result