class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += i + 1
        
        return count


        