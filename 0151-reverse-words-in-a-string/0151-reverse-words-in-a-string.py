class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        temp = ""
        
        for letter in s:
            if letter != " ":
                temp += letter 
            elif temp != "":
                result.append(temp)
                temp = ""

        if temp != "":
            result.append(temp)
        
        return " ".join(result[::-1])