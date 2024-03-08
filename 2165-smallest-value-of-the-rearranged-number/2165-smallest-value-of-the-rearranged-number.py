class Solution:
    def smallestNumber(self, num: int) -> int:

        if num > 0:
            nums = [digit for digit in str(num)]
            nums.sort()
        else:
            num = abs(num)
            nums = [digit for digit in str(num)]
            nums.sort(reverse=True)

            result = ''
            for digit in nums:
                result += digit
            
            result = '-' + result
            return int(result)

        if nums[0] == '0':
            for i in range(1, len(nums)):
                if nums[i] != '0':
                    nums[0], nums[i] = nums[i], nums[0]
                    break
        
        result = ''
        for digit in nums:
            result += digit
    
        return int(result)

        