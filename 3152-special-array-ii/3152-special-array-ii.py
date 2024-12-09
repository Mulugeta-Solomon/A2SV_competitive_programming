class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        if len(queries) == 1:
            left, right = queries[0]
            if right - left + 1 == 1:
                return [True]
            
        prefix_sum = [0] * (len(nums) + 1)
        prefix_sum[0] = 0
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        result = [None] * len(queries)
        
        for i in range(len(queries)):
            left, right = queries[i]
            check = right - left + 1
            
            if check == 2:
                result[i] = (prefix_sum[right] - prefix_sum[left - 1]) % 2 != 0
                    
            if check == 3:
                for j in range(left + 1, right + 1):
                    if nums[j-1] % 2 == 0 and nums[j] % 2 != 0:
                        result[i] == True
                    elif nums[j-1] % 2 != 0 and nums[j] % 2 == 0:
                        result[i] == True
                    else:
                        result[i] =  False
                        break
                    
            else:         
                if nums[left] % 2 == 0:
                    if check % 2 == 0:
                        result[i] = (prefix_sum[right] - prefix_sum[left - 1]) % 2 != 0
                    else:
                        result[i] = (prefix_sum[right] - prefix_sum[left - 1]) % 2 == 0
                else:
                    if check % 2 == 0:
                        result[i] = (prefix_sum[right] - prefix_sum[left - 1]) % 2 == 0
                    else:
                        result[i] = (prefix_sum[right] - prefix_sum[left - 1]) % 2 != 0           
        
        return result
        