class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            
        look_up, result = [0] * len(points) , [0] * k

        for i in range(len(points)):
            x, y = points[i]
            dist = x ** 2 + y ** 2
            look_up[i] = [dist, i]

        look_up.sort()

        for i in range(k):
            result[i] = points[look_up[i][1]]

        return result
