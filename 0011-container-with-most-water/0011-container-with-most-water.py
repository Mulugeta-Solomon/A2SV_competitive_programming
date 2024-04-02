class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right, max_area = 0, len(height) - 1, 0
        max_height = max(height)

        while left < right:
            height_ = min(height[left], height[right])
            width = right - left
            curr_area = height_ * width 
            max_area = max(max_area, curr_area)

            if max_height * width <= max_area:
                break

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        