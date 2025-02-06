class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result, curr = [0] * len(queries), sum([num for num in nums if not (num % 2)])
        print(curr)

        for i, (val, idx) in enumerate(queries):
            if nums[idx] % 2 == 0 and val % 2 == 0:
                curr += val
                result[i] = curr
            elif nums[idx] % 2 == 1 and val % 2 == 1:
                curr += (nums[idx] + val)
                result[i] = curr
            else:
                if nums[idx] % 2 == 0:
                    curr -= nums[idx]  
                result[i] = curr
            
            nums[idx] += val
        
        return result