class AllOne:

    def __init__(self):
        self.data = defaultdict(int)

    def inc(self, key: str) -> None:
        self.data[key] += 1

    def dec(self, key: str) -> None:
        self.data[key] -= 1
        if self.data[key] == 0:
            del self.data[key]

    def getMaxKey(self) -> str:
        if not self.data:
            return ''
        
        result, maxVal = '', 0
        for key, count in self.data.items():
            if count > maxVal:
                maxVal = count
                result = key
        
        return result

    def getMinKey(self) -> str:
        if not self.data:
            return ''
        
        result, minVal = '', float('inf')
        for key, count in self.data.items():
            if minVal > count:
                minVal = count
                result = key
        
        return result
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()