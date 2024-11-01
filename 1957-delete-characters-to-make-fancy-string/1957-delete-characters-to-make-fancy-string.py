class Solution:
    def makeFancyString(self, s: str) -> str:

        result, count = s[0], 1
        curr = s[0]

        for char in s[1:]:
            if curr == char:
                count += 1
            else:
                curr = char 
                count = 1

            if count < 3:
                result += char 
        
        return result 


        