# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedlist = []
        self.ptr = 0
    
        def recurr(node):
            for nested in node:
                if nested.isInteger():
                    self.nestedlist.append(nested.getInteger())
                    continue
                recurr(nested.getList())
            
        recurr(nestedList)
        
    def next(self) -> int: 
        curr = self.nestedlist[self.ptr]
        self.ptr += 1
        return curr    
        
    def hasNext(self) -> bool:
        return self.ptr < len(self.nestedlist)
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())