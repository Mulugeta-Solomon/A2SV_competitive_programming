class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(n):
            curr_sum = 0
            for val in nums:
                curr_sum += ceil(val/n)
            return curr_sum 
        
        left, right = min(nums), max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid) > threshold:
                result = left
                left = mid + 1
            else:
                right = mid - 1
        
        return result + 1