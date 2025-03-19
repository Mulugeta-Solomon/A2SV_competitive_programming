class Solution:
    def checkRecord(self, s: str) -> bool:
        counter = Counter(s)
        if counter['A'] >= 2:
            return False
        
        late, curr = 0, 1 if s[0] == 'L' else 0
        for i in range(1, len(s)):
            if s[i - 1] == 'L':
                if s[i] == 'L':
                    curr += 1
                late = max(late, curr)
                continue
            if s[i] == 'L':
                curr = 1 
            late = max(late, curr)
        
        return late < 3
