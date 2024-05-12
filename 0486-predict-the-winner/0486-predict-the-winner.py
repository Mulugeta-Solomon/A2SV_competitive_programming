class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:

        total_score = sum(nums)
        player_1 = self.helper(nums, 0, len(nums) - 1, 0)
        player_2 = total_score - player_1 
        
        return player_1 >= player_2

    
    def helper(self, nums: List[int], left: int , right: int, chance: int) -> int:
        if left > right:
            return 0
        
        if chance == 0:
            return max(nums[left] + self.helper(nums, left + 1, right, 1),
            nums[right] + self.helper(nums, left, right - 1, 1))
        else:
            return min(self.helper(nums, left + 1, right, 0), 
            self.helper(nums, left, right - 1, 0))
        


        

        