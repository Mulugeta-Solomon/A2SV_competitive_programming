class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        n = int(len(nums) / 2) 
        shuffled = []
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])

        return shuffled

        