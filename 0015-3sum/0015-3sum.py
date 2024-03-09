class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1 

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    last_left_occurence, last_right_occurence = nums[left], nums[right]
                    
                    while left < right and nums[left] == last_left_occurence:
                        left += 1

                    while left < right and nums[right] == last_right_occurence:
                        right -= 1 
        
        return result 
               


                



        