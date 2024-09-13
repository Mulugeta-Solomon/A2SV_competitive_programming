class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        k = 2 ** maximumBit - 1
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i] 

        result = []
        for i in range(len(nums) - 1, -1, -1):
            result.append(prefix_xor[i] ^ k)
        
        return result