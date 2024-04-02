class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()

        majority_element = nums[len(nums)//2]
        
        return majority_element
            

