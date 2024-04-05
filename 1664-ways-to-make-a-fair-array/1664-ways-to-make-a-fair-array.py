class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        prefix_sum_odd_before, prefix_sum_even_before = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        prefix_sum_odd_after, prefix_sum_even_after = [0] * (len(nums) + 1), [0] * (len(nums) + 1)

        for i in range(len(nums)):
            if i%2 == 0:
                prefix_sum_even_before[i+1] = prefix_sum_even_before[i-1] + nums[i]
                prefix_sum_odd_before[i+1] = prefix_sum_odd_before[i]
            else:
                prefix_sum_even_before[i+1] = prefix_sum_even_before[i]
                prefix_sum_odd_before[i+1] = prefix_sum_odd_before[i-1] + nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            if i%2 == 0:
                prefix_sum_even_after[i] = prefix_sum_even_after[i+1] + nums[i]
                prefix_sum_odd_after[i] = prefix_sum_odd_after[i+1]
            else:
                prefix_sum_even_after[i] = prefix_sum_even_after[i+1]
                prefix_sum_odd_after[i] = prefix_sum_odd_after[i+1] + nums[i]

        count = 0
        for i in range(len(nums)):

            if i == 0:
                if prefix_sum_odd_after[i+1] == prefix_sum_even_after[i+1]:
                    count += 1
            elif i == len(nums) - 1:
                if prefix_sum_odd_before[i] == prefix_sum_even_before[i]:
                    count += 1
            else:
                if prefix_sum_even_before[i] + prefix_sum_odd_after[i+1] == prefix_sum_even_after[i+1] + prefix_sum_odd_before[i]:
                    count += 1
        
        return count 
            
        
     