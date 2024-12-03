class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result, left = '', 0

        for i, right in enumerate(spaces):
            result += s[left:right] + ' '
            left = right

            if i == len(spaces) - 1:
                result += s[right:]


        return result