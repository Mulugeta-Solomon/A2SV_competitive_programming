class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in VOWELS:
                left += 1
            
            while left < right and s[right] not in VOWELS:
                right -= 1
            
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        s = ''.join(s)
        return s