class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        max_heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                bricks -= diff 
                heappush(max_heap, -diff)

                if bricks < 0:
                    bricks += (-heappop(max_heap))
                    ladders -= 1
                
                if ladders < 0:
                    return i
        
        return len(heights) - 1