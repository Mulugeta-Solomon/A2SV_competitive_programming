class NumberContainers:

    def __init__(self):
        self.container = {}
        self.index_num = {}

    def change(self, index: int, number: int) -> None:
        if number not in self.container:
            self.container[number] = []
        heappush(self.container[number], index)
        self.index_num[index] = number 
        
    def find(self, number: int) -> int:
        if number not in self.container:
            return -1

        while self.container[number] and self.index_num[self.container[number][0]] != number:
            heappop(self.container[number])
        
        return self.container[number][0] if self.container[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)