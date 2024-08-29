class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        curr = x ^ y
        distance = 0
        
        for val in bin(curr):
            if val == '1':
                distance += 1
        
        return distance 