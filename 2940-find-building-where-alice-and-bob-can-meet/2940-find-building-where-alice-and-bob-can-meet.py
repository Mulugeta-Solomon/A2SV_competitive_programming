class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        min_heap, result = [], [-1] * len(queries)
        group = defaultdict(list)

        for i, query in enumerate(queries):
            left, right = sorted(query)

            if left == right or heights[left] < heights[right]:
                result[i] = right
            
            else:
                max_height = max(heights[left], heights[right])
                group[right].append((max_height, i))
        
        for i, height in enumerate(heights):
            for q_height, q_idx in group[i]:
                heappush(min_heap, (q_height, q_idx))

            while min_heap and height > min_heap[0][0]:
                q_height, q_idx = heappop(min_heap)
                result[q_idx] = i
    
        return result 



