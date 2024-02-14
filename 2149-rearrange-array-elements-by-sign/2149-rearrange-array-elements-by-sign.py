class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos_idx = 0
        neg_idx = 1
        result = [0] * len(nums)

        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
        
        return result

        