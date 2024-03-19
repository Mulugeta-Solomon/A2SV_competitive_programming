class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum 
    
        for left in range(len(nums) - k):
            next_sum = curr_sum + (nums[left+k] - nums[left])
            if next_sum > max_sum:
                max_sum = next_sum
            
            curr_sum = next_sum

    
        return max_sum/k 
        