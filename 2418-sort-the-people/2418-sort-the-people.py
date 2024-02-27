class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        name_height_look_up = {}

        for i in range(len(names)):
            name_height_look_up[heights[i]] = names[i]
        
        for i in range(len(heights)):
            for j in range(len(heights) - i - 1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        
        # print(name_height_look_up)
        # print(heights)
        
        result = []
        for height in heights:
            result.append(name_height_look_up[height])
        
        return result


        