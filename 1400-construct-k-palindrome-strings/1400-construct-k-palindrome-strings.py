class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        
        freq, odd_count = defaultdict(int), 0
        for char in s:
            freq[char] += 1
        
        for char, count in freq.items():
            if count % 2 == 1:
                odd_count += 1
        
        return odd_count <= k