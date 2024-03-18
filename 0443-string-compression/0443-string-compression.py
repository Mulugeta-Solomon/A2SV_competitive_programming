class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) == 1:
            return 1
        
        left, result = 0, 0
        
        while left < len(chars):
            curr_char = chars[left]
            count = 0

            while left < len(chars) and curr_char == chars[left]:
                count += 1
                left += 1
            
            chars[result] = curr_char 
            result += 1

            if count > 1:
                for char in str(count):
                    chars[result] = char
                    result += 1
            
        return result 