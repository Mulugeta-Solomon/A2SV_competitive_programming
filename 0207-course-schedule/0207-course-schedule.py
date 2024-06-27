class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        def dfs(curr):
            if curr not in graph:
                return True
            if curr in visited:
                return False

            visited.add(curr)

            for course in graph[curr]:
                if not dfs(course):
                    return False
            
            return True

        visited = set()
        for preq in graph.keys():
            if not dfs(preq):
                return False
        return True
        