class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0

        for num in nums:
            if count == 0 or count == 1 or nums[count-2] != num:
                nums[count] = num
                count += 1

        return count
        