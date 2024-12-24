class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def build_tree(edges: List[List[int]], n: int) -> List[List[int]]:
            tree = [[] for _ in range(n)]
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def diameter(tree: List[List[int]]) -> int:
            node, _ = bfs(tree, 0) # Find the furthest node from arbitrary node
            _, diameter = bfs(tree, node) # Find the diameter starting from the furthest node

            return diameter
            
        def bfs(tree: List[List[int]], source: int):
            queue = deque([source])
            visited, far_node, level = set(), source, 0
            visited.add(source)

            while queue:
                size = len(queue)
                for _ in range(size):
                    curr = queue.popleft()
                    far_node = curr

                    for neighbor in tree[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                if queue:
                    level += 1

            return far_node, level
        
        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)

        diameter1 = diameter(tree1)
        diameter2 = diameter(tree2)

        comb_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, comb_diameter)