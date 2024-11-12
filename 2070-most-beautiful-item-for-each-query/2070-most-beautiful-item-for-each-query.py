class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        lookUp, result = defaultdict(int), [0] * len(queries)

        for price, beauty in items:
            if lookUp[price] < beauty:
                lookUp[price] = beauty
        
        prices = list(sorted(map(int, lookUp.keys())))
        print(lookUp)
        def binarySearch(target, prices):
            left, right = 0, len(prices) - 1

            while left < right:
                mid = left + (right - left) // 2

                if target > prices[mid]:
                    left =  mid + 1 
                else:
                    right = mid 
            
            return left
        print(prices)
        for i in range(len(queries)):
            idx = binarySearch(queries[i], prices)
            # idx = bisect_right(prices, queries[i]) - 1
            # print(idx, queries[i])
            print(i, idx)
            if idx < 0:
                if queries[i] >= prices[0]:
                    result[i] = lookUp[prices[0]]
            elif idx > len(prices):
                if queries[i] >= prices[-1]:
                    result[i] = lookUp[prices[-1]]
            else:
                if queries[i] >= prices[idx]:
                    result[i] = lookUp[prices[idx]]
                else:
                    if idx > 0:
                        result[i] = lookUp[prices[idx - 1]]

        return result