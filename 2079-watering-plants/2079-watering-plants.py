class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps = 0
        max_capacity = capacity

        for i in range(len(plants)):

            if capacity >= plants[i]:
                capacity = capacity - plants[i]
                steps += 1
            else:
                capacity = max_capacity - plants[i]
                steps += (2*i + 1)
        
        return steps


        