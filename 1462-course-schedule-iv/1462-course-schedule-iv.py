class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque() 

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        
        prereq = defaultdict(set)

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neigh in graph[node]:
                    prereq[neigh].add(node)

                    for pre in prereq[node]:
                        prereq[neigh].add(pre)
                    
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
        
        result = [None] * len(queries)
        for i, (u, v) in enumerate(queries):
            result[i] = u in prereq[v]
        
        return result