class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        result = []
        for i in range(len(boxes)):
            counter = 0
            for j in range(len(boxes)):
                if (i != j) and boxes[j] == "1":
                    counter += abs(i-j)
            
            result.append(counter)
        
        return result

        