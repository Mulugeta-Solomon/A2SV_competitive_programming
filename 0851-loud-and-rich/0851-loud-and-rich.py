class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * len(quiet)

        for src, dst in richer:
            graph[src].append(dst)
            indegree[dst] += 1
        queue, result = deque(), [i for i in range(len(quiet))]
        print(result)

        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if quiet[result[neighbor]] > quiet[result[node]]:
                        result[neighbor] = result[node]
                    
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        return result
        