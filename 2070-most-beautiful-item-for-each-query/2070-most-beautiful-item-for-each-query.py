class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        curr_max, result = 0, [0] * len(queries)

        for i in range (len(items)):
            curr_max = max(curr_max, items[i][1])
            items[i][1] = curr_max

        def binarySearch(items, target):
            left, right, result = 0, len(items) - 1, 0

            while left <= right:
                mid = left + (right - left) // 2

                if items[mid][0] > target:
                    right =  mid - 1 
                else:
                    result = max(result, items[mid][1])
                    left = mid + 1
    
            return result

        for i in range(len(queries)):
            curr = binarySearch(items, queries[i])
            if curr > 0:
                result[i] = curr

        return result