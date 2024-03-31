class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        lookup, majority_element = {}, 0

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        
        for num, freq in lookup.items():
            if freq > len(nums)//2:
                majority_element = num
        
        return majority_element
            

