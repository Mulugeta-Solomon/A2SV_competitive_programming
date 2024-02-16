class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = []
        greatest = max(candies)

        for candie in candies:
            result.append((candie + extraCandies) >= greatest)
        
        return result
        