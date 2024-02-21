class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        look_up_1 = {}
        look_up_2 = {}

        for word in words1:
            if word not in look_up_1:
                look_up_1[word] = 1
            else:
                look_up_1[word] += 1

        for word in words2:
            if word not in look_up_2:
                look_up_2[word] = 1
            else:
                look_up_2[word] += 1
        
        counter = 0
        for word, freq in look_up_1.items():
            if freq == 1 and word in look_up_2:
                if look_up_2[word] == 1:
                    counter += 1
        
        return counter


        