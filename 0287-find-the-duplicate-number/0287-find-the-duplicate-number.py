class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        bit_nums = {}

        for i in range(len(nums)):
            if nums[i] not in bit_nums:
                bit_nums[nums[i]] = 1
            else:
                bit_nums[nums[i]] += 1

        for num, freq in bit_nums.items():
            if freq > 1:
                return num

        