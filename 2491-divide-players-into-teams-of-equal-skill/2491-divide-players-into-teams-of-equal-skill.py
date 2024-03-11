class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        chemistry = 0
        left, right = 0, len(skill) - 1

        while left < right:
            curr_sum = skill[left] + skill[right]
            
            if left == 0 or curr_sum == last_sum:
                chemistry += (skill[left] * skill[right])
                last_sum = curr_sum
                left += 1
                right -= 1
            else:
                return -1
        
        return chemistry
        