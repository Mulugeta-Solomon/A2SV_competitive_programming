class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         
         '''
         nums = [4,5,0,-2,-3,1], k = 5
        prefix_sum = [4, 9, 9, 7, 4, 5]
        
        remaider = [4, 4 , 4, 2, 4, 0 ]
         '''

         remainder = {0:1}
         prefix_sum, max_subarr = 0, 0
         for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum % k in remainder:
                max_subarr += remainder[prefix_sum % k]

            remainder[prefix_sum % k] = remainder.get(prefix_sum % k, 0) + 1
         print(remainder)
         return max_subarr