class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-freq, char] for char, freq in count.items()]
        heapify(max_heap)
        
        result = ''

        while max_heap:
            if len(max_heap) == 1:
                freq, char = heappop(max_heap)
                if -freq > 1:
                    return ''
                return result + char

            freq1, char1 = heappop(max_heap)
            freq2, char2 = heappop(max_heap)
            freq1, freq2 = -freq1, -freq2

            result += char1 + char2
            
            if freq1 > 1:
                heappush(max_heap, [-(freq1 - 1), char1])
            if freq2 > 1:
                heappush(max_heap, [-(freq2 - 1), char2])

        return result