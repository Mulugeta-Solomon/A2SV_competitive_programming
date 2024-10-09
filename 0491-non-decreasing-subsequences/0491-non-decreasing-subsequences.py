class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result, curr = defaultdict(int), []
        
        def backtrack(idx):
            if len(curr) > 1:
                if tuple(curr) not in result:
                    result[tuple(curr)] = 1
            

            for i in range(idx, len(nums)):
                if not curr or nums[i] >= curr[-1]:
                    curr.append(nums[i])
                    backtrack(i + 1) 
                    curr.pop()
                

        backtrack(0)

        return result

