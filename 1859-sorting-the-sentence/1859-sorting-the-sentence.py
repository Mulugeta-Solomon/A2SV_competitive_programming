class Solution:
    def sortSentence(self, s: str) -> str:
                
        result = []
        look_up = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        i, curr = 0, ''
        while i < len(s):
            if s[i] in look_up:
                result.append([int(s[i]), curr])
                curr = ''
            elif s[i] == ' ':
                i += 1
                continue
            else:
                curr += s[i]
            i += 1
        
        result.sort()
        ans = ''
        for i in range(len(result)):
            if i == 0:
                ans += result[i][1]
            else:
                ans += ' ' + result[i][1]
        
        return ans

