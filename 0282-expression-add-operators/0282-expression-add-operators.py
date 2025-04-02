class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def dfs(idx, curr_res, curr_sum, prev):
            if idx >= len(num):
                if curr_sum == target:
                    result.append(''.join(curr_res[:]))
                    return 
            
            for i in range(idx, len(num)):
                curr = num[idx:i+1]
                curr_num = int(curr)
                if not curr_res:
                    dfs(i + 1, [curr], curr_num, curr_num)
                else:
                    dfs(i + 1, curr_res + ['+'] + [curr], curr_sum + curr_num, curr_num)
                    dfs(i + 1, curr_res + ['-'] + [curr], curr_sum - curr_num, -curr_num)
                    dfs(i + 1, curr_res + ['*'] + [curr], curr_sum - prev + curr_num * prev, curr_num * prev)
                
                if num[idx] == '0':
                    break
        
        result = []
        dfs(0, [], 0, 0)

        return result