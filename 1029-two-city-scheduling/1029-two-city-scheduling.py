class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityB, min_cost = [], 0

        for a, b in costs:
            min_cost += a
            cityB.append(b-a)
        
        cityB.sort()

        for i in range(len(costs) // 2):
            min_cost += cityB[i]
        
        return min_cost

