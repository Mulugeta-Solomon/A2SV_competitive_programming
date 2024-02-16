class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        look_up = {}
        for idx, num in enumerate(nums):
            look_up[num] = look_up.get(num, 0) + 1
        
        result = []

        for num, idx in look_up.items():
            if idx > (n//3):
                result.append(num)
        
        return result

        