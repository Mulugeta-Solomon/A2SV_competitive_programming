class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        result = nums
        nums, curr = sorted(nums), 0
        num_group, group = {nums[0]: curr}, {curr: deque([nums[0]])}

        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > limit:
                curr += 1
            
            if curr not in group:
                group[curr]= deque()
            group[curr].append(nums[i + 1])
            
            num_group[nums[i + 1]] = curr

        for i in range(len(nums)):
            curr_G = num_group[result[i]]
            result[i] = group[curr_G].popleft()
        
        return result

                