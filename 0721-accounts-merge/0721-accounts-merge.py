class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    # def find(self, x):
    #     if x == self.root[x]:
    #         return x
    #     self.root[x] = self.find(self.root[x])
    #     return self.root[x]

    def find(self, x): # Iterative way of path compression 
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = UnionFind(len(accounts))
        email_acc = {}
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_acc:
                    graph.union(i, email_acc[email])
                else:
                    email_acc[email] = i
        
        lookUp = defaultdict(list) # email group idx acc -> list of emails
        for email, i in email_acc.items():
            root = graph.find(i)
            lookUp[root].append(email)
        
        result = []
        for i, emails in lookUp.items():
            account = accounts[i][0]
            result.append([account] + sorted(emails))
        
        return result
