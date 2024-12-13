class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))

        result, visited, directions = 0, set(), [1, -1]

        while heap:
            curr, idx = heappop(heap)
            if idx not in visited:
                result += curr
                for dr in directions:
                    newIdx = idx + dr
                    if 0 <= newIdx < len(nums):
                        visited.add(newIdx) 
        
        return result 