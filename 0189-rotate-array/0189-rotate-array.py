class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k %= len(nums)

        if k > 0:
            self.rotate_(nums, 0, len(nums) - 1) #entire array
            self.rotate_(nums, 0, k - 1) # upto k element
            self.rotate_(nums, k, len(nums) - 1) # the rest of the element

    def rotate_(self, nums, start, end): # simple rotation function
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums



        