class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        sum_ = sum(nums)
        ite, target = target // sum_, target % sum_

        look_up, prefix_sum, len_min_subarr = {0: -1}, 0, float('inf')

        for i in range(len(nums) * 2):
            prefix_sum += nums[i % len(nums)]
            look_up[prefix_sum] = i
            if prefix_sum - target in look_up:
                len_min_subarr = min(len_min_subarr, i - look_up[prefix_sum - target])
        
        len_min_subarr += ite * len(nums)
        if len_min_subarr == float('inf'):
            return -1
        
        return len_min_subarr

        