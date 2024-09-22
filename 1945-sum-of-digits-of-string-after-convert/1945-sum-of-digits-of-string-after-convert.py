class Solution:
    def getLucky(self, s: str, k: int) -> int:
         
        while k >= 0:
            curr = ''
            for i in range(len(s)):
                if s[i].isdigit():
                    if len(curr) == 0:
                        curr += s[i]
                        continue
                    curr = str(int(curr) + int(s[i]))
                    continue
                curr += str(ord(s[i]) - 96)    

            s = str(curr)
            k -= 1
        
        return int(curr)