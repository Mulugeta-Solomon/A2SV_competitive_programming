class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        prefix_sum = [0] * (len(words) + 1)
        look_up = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        for i in range(len(words)):
            if words[i][0] in look_up and words[i][-1] in look_up:
                prefix_sum[i+1] = prefix_sum[i] + 1
            else:
                prefix_sum[i+1] = prefix_sum[i]

        result = [0] * len(queries)

        for i in range(len(queries)):
            left, right = queries[i]
            result[i] = prefix_sum[right+1] - prefix_sum[left]
        
        return result 