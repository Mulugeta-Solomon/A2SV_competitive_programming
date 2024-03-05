class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()        
        pairs = []

        i = 0
        j = len(nums) - 1

        while i < (len(nums)//2):
            pairs.append((nums[i], nums[j]))
            i += 1
            j -= 1
        
        max_pair_sum = float('-inf')

        for pair in pairs:
            max_pair_sum = max(max_pair_sum, sum(pair))

        return max_pair_sum
        