class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        look_up_1 = {}
        look_up_2 = {}

        for word in words1:
            look_up_1[word] = look_up_1.get(word, 0) + 1

        for word in words2:
            look_up_2[word] = look_up_2.get(word, 0) + 1 
        
        counter = 0
        for word, freq in look_up_1.items():
            if freq == 1 and word in look_up_2:
                if look_up_2[word] == 1:
                    counter += 1
        
        return counter


        