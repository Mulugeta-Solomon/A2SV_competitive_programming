class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right, left = len(numbers) - 1, 0

        while left < right:
            temp = numbers[left] + numbers[right] 
            
            if temp == target:
                return [left + 1, right + 1]

            if temp > target:
                right -= 1
            else:
                left += 1
        