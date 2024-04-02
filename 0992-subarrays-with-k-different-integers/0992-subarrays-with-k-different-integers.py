class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        len_withatmost_k = self.subarraywith_atmost_k(nums, k)
        len_with_oneless_k = self.subarraywith_atmost_k(nums, k-1)

        return len_withatmost_k - len_with_oneless_k

    def subarraywith_atmost_k(self, arr, k):
        look_up = {}

        left, max_subarr = 0, 0

        for right in range(len(arr)):
            look_up[arr[right]] = look_up.get(arr[right], 0) + 1

            while len(look_up) > k:
                look_up[arr[left]] -=  1
                if look_up[arr[left]] == 0:
                    del look_up[arr[left]]
                left += 1
            
            max_subarr += right - left + 1 

        return max_subarr





             
