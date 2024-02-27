class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        name_height_look_up = {}

        for i in range(len(names)):
            name_height_look_up[heights[i]] = names[i]
        
        for i in range(1, len(heights)):
            curr_value = heights[i]
            j = i - 1

            while j >= 0 and curr_value > heights[j]:
                heights[j+1] = heights[j]
                j -= 1
            
            heights[j+1] = curr_value

        # print(name_height_look_up)
        # print(heights)
        
        result = []
        for height in heights:
            result.append(name_height_look_up[height])
        
        return result


        