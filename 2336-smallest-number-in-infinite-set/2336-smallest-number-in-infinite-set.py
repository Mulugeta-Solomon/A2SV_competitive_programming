class SmallestInfiniteSet:

    def __init__(self):
        self.smallestInfiniteSet = []
        self.lookUp = set(i for i in range(1, 1001))
        
        for num in range(1, 1001):
            heappush(self.smallestInfiniteSet, num)
        
    def popSmallest(self) -> int:
        small = heappop(self.smallestInfiniteSet)
        self.lookUp.remove(small)
        return small
        
    def addBack(self, num: int) -> None:
        if num not in self.lookUp:
            heappush(self.smallestInfiniteSet, num)
            self.lookUp.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)