class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x 

        while left <= right:
            mid = left + (right - left) // 2
            if x // mid == mid:
                return mid
            if x // mid < mid:
                right = mid - 1
            else:
                left = mid + 1 
        
        return right 