class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0

        for i, num in enumerate(arr):
            left, right = i, len(arr) - i - 1
            result += num * (left // 2 + 1) * (right // 2 + 1)
            result += num * ((left + 1) // 2) * ((right + 1) // 2)

        return result