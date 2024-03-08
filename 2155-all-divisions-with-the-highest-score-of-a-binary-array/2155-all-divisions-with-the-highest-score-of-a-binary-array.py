class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        max_score = float('-inf')
        score_idx = {}

        nums_left = 0
        nums_right = nums.count(1)
        temp = nums_left + nums_right
        score_idx[0] = temp
        max_score = max(float('-inf'), temp)

        for i in range(0, len(nums)):
            if nums[i] ==  0:
                nums_left += 1
            if nums[i] == 1:
                nums_right -= 1

            temp = nums_left + nums_right
            score_idx[i+1] = temp
            max_score = max(max_score, temp)
            
        index = []
        for idx, value in score_idx.items():
            if value == max_score:
                index.append(idx)

        return index