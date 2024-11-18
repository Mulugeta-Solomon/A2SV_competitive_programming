class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result
        
        if k > 0:
            for i in range(len(code)):
                j, count, curr = i + 1, 0, 0
                while count < k:
                    if j == i:
                        j += 1
                        continue
                    if j > len(code) - 1:
                        j = 0
                    
                    curr += code[j]
                    count += 1
                    j += 1

                result[i] = curr
            
        else:
            for i in range(len(code)):
                j, count, curr = i - 1, 0, 0
                while count < -k:
                    if j == i:
                        j -= 1
                        continue
                    if j < 0:
                        j = len(code) - 1

                    curr += code[j]
                    count += 1
                    j -= 1
                
                result[i] = curr
        
        return result
                    

