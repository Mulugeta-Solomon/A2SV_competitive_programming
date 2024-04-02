class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first_ptr, second_ptr, result = 0, 0, []

        while first_ptr < len(firstList) and second_ptr < (len(secondList)):
            first, second = firstList[first_ptr], secondList[second_ptr]
            
            if first[1] < second[0]:
                first_ptr += 1
                continue 
            if first[0] > second[1]:
                second_ptr += 1
                continue

            result.append([max(first[0], second[0]), min(first[1], second[1])])
            
            if first[1] > min(first[1], second[1]):
                second_ptr += 1
            else:
                first_ptr += 1
        
        return result 




