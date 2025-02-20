class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lookup, result = set(), []
        
        for num in nums:
            if num in lookup:
                result.append(num)
            
            lookup.add(num)
            if len(result) == 2:
                return result 
        
        return result 