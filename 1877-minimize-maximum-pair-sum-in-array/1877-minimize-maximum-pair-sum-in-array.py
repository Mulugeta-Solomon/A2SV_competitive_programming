class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size=len(nums)//2
        l=[]
        for i in range(size):
            l.append((nums[i]+nums[len(nums)-i-1]))
        return max(l)
        