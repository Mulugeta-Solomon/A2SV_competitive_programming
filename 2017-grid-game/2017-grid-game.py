class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        pref_row1, pref_row2 = [0] * (col + 1), [0] * (col + 1)
        
        for c in range(col):
            pref_row1[c + 1] = pref_row1[c] + grid[0][c]
            pref_row2[c + 1] = pref_row2[c] + grid[1][c]
        
        pivot, max_point = -1, float('-inf') # point collected by robot_1 
        for i in range(1, col + 1):
            curr = pref_row1[i] + (pref_row2[-1] - pref_row2[i - 1])
            if curr > max_point:
                max_point = curr
                pivot = i
        result = 0
        if pivot == 1:
            result = max(result, pref_row1[-1] - pref_row1[1])
            return result 
        if pivot == col:
            result = max(result, pref_row2[-2])
            return result
        print(pref_row1)
        print(pref_row2)
        print(pivot)
        for i in range(1, col + 1):
            curr = 0
            if i < pivot:
                curr = pref_row2[pivot - 1] - pref_row2[i]
            elif i > pivot:
                curr = pref_row1[i] - pref_row1[pivot]
    
            result = max(result, curr)
        
        return result 


            

