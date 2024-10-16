class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, heap = '', []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heappush(heap, (count, char)) # max heap
        
        while heap:
            count, char = heappop(heap)
            
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not heap:
                    break
                
                count1, char1 = heappop(heap)
                result += char1
                count1 += 1
                if count1:
                    heappush(heap, (count1, char1))
            else:
                result += char
                count += 1
            
            if count:
                heappush(heap, (count, char))
        
        return result

