class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if k <= numOnes:
            return k
        else:
            if k <= numOnes + numZeros:
                return numOnes
            else:
                return (2 * numsOnes + numZeros) - k