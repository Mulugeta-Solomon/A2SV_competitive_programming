class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def isPossible (maxBalls):
            totalOperations = 0
            for num in nums:
                currOp = ceil(num / maxBalls) - 1
                totalOperations += currOp

                if totalOperations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left 