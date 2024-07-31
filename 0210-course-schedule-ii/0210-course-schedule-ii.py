class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for des, src in prerequisites:
            graph[src].append(des)
            indegree[des] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            size = len(queue)
            for _ in range(size):
                src = queue.popleft()
                result.append(src)

                for dst in graph[src]:
                    indegree[dst] -= 1
                    if indegree[dst] == 0:
                        queue.append(dst)
        
        if len(result) != numCourses:
            return []
        
        return result 


