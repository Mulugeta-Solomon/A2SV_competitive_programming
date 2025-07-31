class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph, n = defaultdict(list), len(ingredients)
        indegree = [len(ingredients[i]) for i in range(n)] 

        for i in range(n):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(i)
        
        queue, result = deque(supplies), []
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for recipe in graph[curr]:
                    indegree[recipe] -= 1
                    if not indegree[recipe]:
                        queue.append(recipes[recipe])
                        result.append(recipes[recipe])

        return result