class Solution:
    def trap(self, height: List[int]) -> int:

        left, right, trap_water = 0, len(height) - 1, 0
       
        while left < right:
            if height[left] < height[right]:
                min_height_left = height[left]
                bucket, water, location_left = 0, 0, left

                while left < right:
                    if height[left] < min_height_left:
                        bucket += (min_height_left - height[left])
                    else:
                        min_height_left = height[left]
                        water += bucket
                        bucket = 0
                        location_left = left
                    left += 1

                if min_height_left <= height[right]:
                    water += bucket
                else:
                    left = location_left

            else:
                min_height_right = height[right]
                bucket, water, location_right = 0, 0, right

                while left < right:
                    if height[right] < min_height_right:
                        bucket += (min_height_right - height[right])
                    else:
                        min_height_right = height[right]
                        water += bucket
                        bucket = 0
                        location_right = right
                    right -= 1
                
                if min_height_right <= height[left]:
                    water += bucket
                else:
                    right = location_right
            

            trap_water += water

        return trap_water