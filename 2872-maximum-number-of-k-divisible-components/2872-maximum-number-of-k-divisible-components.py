class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree, result = defaultdict(list), [0]
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(curr, parent, result):
            sum_ = 0

            for neighbor in tree[curr]:
                if neighbor != parent:
                    sum_ += dfs(neighbor, curr, result)
                    
                    sum_ %= k

            sum_ += values[curr]
            sum_ %= k

            if sum_ == 0:
                result[0] += 1
            
            return sum_
            
        dfs(0, -1, result)
        
        return result[0]
        