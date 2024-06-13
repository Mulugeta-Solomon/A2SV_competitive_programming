class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        candidate = set()

        for edge in edges:
            a, b  = edge
            candidate.add(a)

        for edge in edges:
            a, b = edge
            if b in candidate:
                candidate.remove(b)
        
        return [i for i in candidate]
            
        
