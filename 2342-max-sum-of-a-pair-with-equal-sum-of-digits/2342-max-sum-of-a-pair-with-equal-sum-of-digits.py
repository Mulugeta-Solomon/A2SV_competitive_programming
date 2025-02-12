class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        lookup, result = defaultdict(list), -1

        def digit_sum(num):
            result = 0
            while num > 0:
                result += (num % 10)
                num //= 10
            return result

        for num in nums:
            curr = digit_sum(num)
            if curr in lookup:
                prev = -heappop(lookup[curr])
                result = max(result, num + prev)
                heappush(lookup[curr], -prev)
            heappush(lookup[curr], -num)

        return result