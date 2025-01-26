class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        indegree = [0] * len(favorite)

        for person in range(len(favorite)):
            indegree[favorite[person]] += 1 # calculate indegree
        
        # Topo sort to remove the non-cycle
        queue = deque()
        for person in range(len(favorite)):
            if indegree[person] == 0:
                queue.append(person)
        
        depth = [1] * len(favorite) # depth of each node

        while queue:
            size = len(queue)
            for _ in range(size):
                curr_node = queue.popleft()
                next_node = favorite[curr_node]
                depth[next_node] = max(depth[next_node], depth[curr_node] + 1)
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        
        longest_cycle, two_cycle = 0, 0
        # detect cycle
        for person in range(len(favorite)):
            if indegree[person] != 0:
                cycle_len, curr = 0, person

                while indegree[curr] != 0:
                    indegree[curr] = 0 # visited
                    cycle_len += 1
                    curr = favorite[curr]
                
                if cycle_len == 2:
                    # for 2 cycle add the depth of both nodes 
                    two_cycle += depth[person] + depth[favorite[person]]
                else:
                    longest_cycle = max(longest_cycle, cycle_len)

        return max(longest_cycle, two_cycle)   

