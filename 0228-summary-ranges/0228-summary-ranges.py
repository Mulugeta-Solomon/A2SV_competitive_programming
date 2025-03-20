class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result, curr = [], f'{str(nums[0])}'
        left = 0
        for right in range(1, len(nums)):
            if nums[right - 1] + 1 == nums[right]:
                if right == len(nums) - 1:
                    curr += '->' + str(nums[right])
                continue
            else:
                if nums[left] == nums[right - 1]:
                    result.append(curr)
                else:
                    curr += '->' + str(nums[right - 1])
                    result.append(curr)
                left = right
                curr = str(nums[right])
 
        result.append(curr)
        return result
            
