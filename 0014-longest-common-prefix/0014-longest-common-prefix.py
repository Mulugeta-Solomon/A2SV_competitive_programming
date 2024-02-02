class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take the first value as common prefix
        common_prefix = strs[0]

        for word in strs:
            # compare and replace the common prefix with the shortest word in the strs list
            if len(common_prefix) > len(word):
                common_prefix, word = word, common_prefix
            
            while len(common_prefix) > 0:
                # compre if the sliced word is same as the common prefix else drop the last word and check again 
                if word[:len(common_prefix)] == common_prefix:
                    break 
                else: 
                    common_prefix = common_prefix[:-1]
        
        return common_prefix 
            
