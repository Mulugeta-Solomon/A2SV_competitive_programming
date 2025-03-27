class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev == None:
                    prev = i
                    continue
                if i - prev - 1 >= k:
                    prev = i
                else:
                    return False 

        return True