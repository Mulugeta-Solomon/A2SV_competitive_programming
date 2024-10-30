class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis, lds = [0] * len(nums), [0] * len(nums)
        lis[0], lds[-1] = 1, 1
        
        for i in range(1, len(nums)):
            curr = 0
            for j in range(i) :
                if nums[i] > nums[j]:
                    curr = max(curr, lis[j])
            lis[i] = curr + 1
        
        for i in range(len(nums) - 2, - 1, - 1):
            curr = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    curr = max(curr, lds[j])
            lds[i] = curr + 1
        
        result = float('inf')
        for i in range(1, len(nums) - 1):
            if lis[i] > 1 and lds[i] > 1:
                result = min(result, len(nums) - lis[i] - lds[i] + 1)

        return result

        