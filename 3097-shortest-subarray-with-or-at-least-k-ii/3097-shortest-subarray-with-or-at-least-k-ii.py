class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits, currOr, left, result = [0] * 32, 0, 0, float('inf')

        for right in range(len(nums)):
            currOr |= nums[right]

            for bit in range(32):
                if nums[right] & (1 << bit):
                    bits[bit] += 1

            while left <= right and currOr >= k:
                result = min(result, right - left + 1)
                newOr = 0
                for bit in range(32):
                    if nums[left] & (1 << bit):
                        bits[bit] -= 1
                    if bits[bit] > 0:
                        newOr |= (1 << bit)
                currOr = newOr
                left += 1
        
        return result if result != float('inf') else -1