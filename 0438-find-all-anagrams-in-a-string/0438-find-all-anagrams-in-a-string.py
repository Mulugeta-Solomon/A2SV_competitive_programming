class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_dict = {}
        for str_ in p:
            p_dict[str_] = p_dict.get(str_, 0) + 1
        
        k = len(p)         
        result = []
        
        curr_str = {}
        for i in range(0, k):
            curr_str[s[i]] = curr_str.get(s[i], 0) + 1
        
        for left in range(len(s) - k + 1):
            if curr_str == p_dict:
                result.append(left)
            
            if left == len(s) - k:
                break

            curr_str[s[left]] = curr_str.get(s[left], 0) - 1
            if curr_str[s[left]] <= 0:
                del curr_str[s[left]]
            
            curr_str[s[left+k]] = curr_str.get(s[left+k], 0) + 1

        return result


 

