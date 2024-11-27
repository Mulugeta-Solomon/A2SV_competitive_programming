class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n

        for u, v in edges:
            indegree[v] += 1
        
        result, count = -1, 0
        for node, degree in enumerate(indegree):
            if degree == 0:
                result = node
                count += 1
                if count > 1:
                    return -1
        
        return result 
                

        