class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        numSetbits = defaultdict(int)

        for num in nums:
            numSetbits[num] = bin(num).count('1')

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    if numSetbits[nums[j]] != numSetbits[nums[j+1]]:
                        return False
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return True