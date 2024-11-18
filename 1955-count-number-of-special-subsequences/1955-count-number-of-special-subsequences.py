class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        zeros, ones, twos = 0, 0, 0

        for n in nums:
            if n == 0:
                zeros += (zeros + 1) % MOD
            elif n == 1:
                ones += (ones + zeros) % MOD
            else:
                twos += (twos + ones) % MOD
        
        return twos 

