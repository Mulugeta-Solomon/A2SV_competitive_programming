class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result, left, space = '', 0, ' '

        for i, right in enumerate(spaces):
            result += s[left:right] + space
            left = right

            if i == len(spaces) - 1:
                result += s[right:]


        return result