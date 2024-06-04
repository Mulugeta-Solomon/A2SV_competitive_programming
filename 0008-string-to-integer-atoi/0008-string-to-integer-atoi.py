class Solution:
    def myAtoi(self, s: str) -> int:
        look_up = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        result = ''
        MIN, MAX = -2**31, 2**31 - 1

        for i in range(len(s)):
            if s[i] == ' ':
                if i > 0 and len(result) > 0:
                    break
                continue

            if i == 0 and s[i] not in look_up:
                if s[i] == '-' or s[i] == '+':
                    result += s[i]
                    continue
                else:
                    break
            if i > 0 and s[i] not in look_up:
                if len(result) == 0 and (s[i] == '-' or s[i] == '+'):
                    if s[i-1] != '+':
                        result += s[i]
                        continue
                    else:
                        break
                else:
                    break
            
            result += s[i]

        if len(result) == 0 or (len(result) == 1 and (result[-1] == '-' or result[-1] == '+')):
            return 0
        if int(result) < MIN:
            return MIN
        if int(result) > MAX:
            return MAX
        
        return int(result)
        