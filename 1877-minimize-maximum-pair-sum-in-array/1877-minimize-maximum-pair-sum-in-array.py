class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()        

        i = 0
        j = len(nums) - 1
        max_pair_sum = float('-inf')

        while i < (len(nums)//2):
            max_pair_sum = max(max_pair_sum, sum([nums[i], nums[j]]))
            i += 1
            j -= 1

        return max_pair_sum
        