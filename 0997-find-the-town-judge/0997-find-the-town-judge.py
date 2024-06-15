class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        result = [False] * n
        graph = defaultdict(list)

        for i in range(len(trust)):
            a, b = trust[i]
            result[a - 1] = True
            graph[b].append(a)

        for i in range(n):
            if not result[i] and len(graph[i + 1]) == n - 1:
                return i + 1
        return -1