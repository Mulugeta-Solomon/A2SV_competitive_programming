class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        look_up = {0:1}
        prefix_sum, max_subarr = 0, 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in look_up:
                max_subarr += look_up[prefix_sum-k]
            
            look_up[prefix_sum] = look_up.get(prefix_sum, 0) + 1
            
        return max_subarr

