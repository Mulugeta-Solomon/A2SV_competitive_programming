class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        result = 0

        for num, freq in Counter(nums).items():
            if freq == 2:
                if result == 0:
                    result = num
                else:
                    result ^= num
        
        return result