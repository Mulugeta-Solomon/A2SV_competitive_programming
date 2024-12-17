class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        heap, result = [], []

        for char, count in counts.items():
            heappush(heap, (-ord(char), count))

        while heap:
            curr, count = heappop(heap)  
            char = chr(-curr)
            repeat = min(count, repeatLimit)
            result.append(char * repeat)

            if heap and count > repeat:
                next, next_count = heappop(heap)
                result.append(chr(-next))
                if next_count > 1:
                    heappush(heap, (next, next_count - 1))
                heappush(heap, (curr, count - repeat))

        result = ''.join(result)
        
        return result
