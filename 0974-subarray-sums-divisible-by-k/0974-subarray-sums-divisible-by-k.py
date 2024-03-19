class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        remainder = [0] * k
        remainder[0] = 1

        curr_remainder = 0

        for num in nums:
            curr_remainder = (num + curr_remainder) % k
            remainder[curr_remainder] += 1
        
        result = sum([n * (n-1) // 2 for n in remainder])
        
        return result