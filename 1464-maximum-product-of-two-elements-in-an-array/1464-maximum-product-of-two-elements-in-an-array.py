class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        first = nums.pop()
        second = nums.pop()
        return (first - 1) * (second - 1)