class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_appeard = {s[i]:i for i in range(len(s))}
        
        first, result = 0, []

        while first < len(s):
            end, second = last_appeard[s[first]], first + 1

            while second < end:
                if last_appeard[s[second]] > end:
                    end = last_appeard[s[second]]
                second += 1
            
            result.append(end - first + 1)
            first = end + 1

        return result 

        