class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]: 
        lower_pivot = []
        higher_pivot = []
        pivots = []
        
        for num in nums:
            if num > pivot:
                higher_pivot.append(num)
            elif num == pivot:
                pivots.append(num)
            else:
                lower_pivot.append(num)
        
        return lower_pivot + pivots + higher_pivot