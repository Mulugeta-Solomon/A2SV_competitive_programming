class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] > 0:
                break
        left, right = nums[:i], nums[i:]
        i, l, r = 0, len(left) - 1, 0

        while l >= 0 and r < len(right):
            if left[l] ** 2 <= right[r] ** 2:
                nums[i] = left[l] ** 2
                l -= 1
                i += 1
            else:
                nums[i] = right[r] ** 2
                r += 1
                i += 1
        
        while l >= 0:
            nums[i] = left[l] ** 2
            i += 1
            l -= 1
        
        while r < len(right):
            nums[i] = right[r] ** 2
            i += 1
            r += 1
        
        return nums