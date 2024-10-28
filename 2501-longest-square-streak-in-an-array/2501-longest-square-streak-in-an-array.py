class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        flag, result = [False] * (max(nums) + 1), -1
        nums.sort()
        for num in nums:
            flag[num] = True
        
        for num in nums:
            curr = 1
            if flag[num]:
                j = num * num
                while j < len(flag) and flag[j]:
                    curr += 1
                    j *= j
            if curr >= 2:
                result = max(result, curr)

        return result
        