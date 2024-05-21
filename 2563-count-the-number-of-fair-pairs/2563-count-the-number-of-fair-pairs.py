class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()

        def _count(a):
            count = 0
            left, right = 0, len(nums) - 1

            while left < right:

                if nums[left] + nums[right] > a:
                    right -= 1
                else:
                    count += right - left
                    left += 1
            
            return count 
        
        count_low = _count(lower - 1)
        count_up = _count(upper)

        return count_up - count_low


        
        