class Solution:
    def countAndSay(self, n: int) -> str:
        
        result = deque()

        for i in range(1, n + 1):
            if i == 1:
                result.append('1')
            
            else:
                main, curr, count = '','', 0
                for i in range(len(result)):
                    if curr and (not result or curr[-1] != result[0]):
                        main += str(count) + curr[0]
                        curr, count = '', 0
                        
                    curr += result.popleft()
                    count += 1          
                
                main += str(count) + curr[0]

                for i in range(len(main)):
                    result.append(main[i])
        
        return ''.join(result)
                    
                
