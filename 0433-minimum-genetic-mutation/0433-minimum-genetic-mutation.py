class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
  
        que = deque([[startGene, 0]])
        ans = 0
        st = set()
        
        def ok(u, v):
            res = 0
            for i in range(len(u)):
                res += int(u[i] != v[i])
            return res == 1
        
        while que:
            u = que.popleft()
            if u[0] == endGene:
                return u[1]
            for v in bank:
                if v not in st:
                    if ok(u[0], v):
                        que.append([v, u[1] + 1])
                        st.add(v)
                        
        return -1
