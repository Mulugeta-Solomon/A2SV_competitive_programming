class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lookUp = {}
        for num in arr:
            lookUp[num] = lookUp.get(num, 0) + 1

        frequency = {}
        for num, freq in lookUp.items():
            if freq in frequency:
                return False
            frequency[freq] = 1
        
        return True


        