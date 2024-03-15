class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first_ptr, second_ptr, result = 0, 0, []

        while first_ptr < len(firstList) and second_ptr < (len(secondList)):
            first_1, second_1 = firstList[first_ptr]
            first_2, second_2 = secondList[second_ptr]

            if first_1 <= second_2 and first_2 <= second_1:
                result.append([max(first_1, first_2), min(second_1, second_2)])
            
            if second_1 <= second_2:
                first_ptr += 1
            else:
                second_ptr += 1
        
        return result 


