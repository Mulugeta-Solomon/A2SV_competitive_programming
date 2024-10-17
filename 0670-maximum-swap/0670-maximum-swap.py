class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        lookUp = {int(val):i for i, val in enumerate(nums)}

        for i, char in enumerate(nums):
            for val in range(9, int(char), -1):
                if lookUp.get(val, -1) > i:
                    nums[i], nums[lookUp[val]] = nums[lookUp[val]], nums[i] 
                    return int(''.join(nums))
        
        return num


        