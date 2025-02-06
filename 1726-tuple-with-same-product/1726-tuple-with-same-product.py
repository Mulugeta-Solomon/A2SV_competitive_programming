class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pair_product, result = defaultdict(int), 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr = nums[i] * nums[j]
                pair_product[curr] += 1

        for prod, freq in pair_product.items():
            equal_pair = (freq - 1) * freq // 2
            result += 8 * equal_pair

        return result
        