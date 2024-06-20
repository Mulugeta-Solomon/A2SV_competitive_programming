class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = {}

        for i in range(len(edges)):
            scores[edges[i]] = scores.get(edges[i], 0) + i
        
        candidate = sorted(scores.keys())
        result = -1
        for edge in candidate:
            if result == -1 or scores[edge] > scores[result]:
                result = edge

        return result
        
