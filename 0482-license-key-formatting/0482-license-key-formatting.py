class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = (''.join(s.split('-'))).upper()
        result = [s[:len(s) % k]]
        print(s)
        for i in range(len(s) % k, len(s), k):
            result.append(s[i:i+k])
        
        if result[0]:
            return '-'.join(result)
            
        return '-'.join(result[1:])