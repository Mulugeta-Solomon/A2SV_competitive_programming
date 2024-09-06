class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set()

        for num in nums:
            result.add(num)
            result.add(int(str(num)[::-1]))
        
        return len(result)

        