class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n, result, i, curr = num_people, [0] * num_people, 0, 1

        while candies > 0:
            if  curr > candies:
                result[i%n] += candies
                break
            result[i % n] += curr
            candies -= curr
            curr += 1
            i += 1
        
        return result
        
        