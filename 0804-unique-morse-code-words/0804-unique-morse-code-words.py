class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookUp = [".-","-...","-.-.","-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        result = set()

        for word in words:
            curr = ''
            for char in word:
                curr += lookUp[ord(char) - ord('a')]
            result.add(curr)

        return len(result)