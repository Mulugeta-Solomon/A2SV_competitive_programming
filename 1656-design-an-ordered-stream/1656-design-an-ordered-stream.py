class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 0
        self.list_strings = [None] * (n + 1)
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list_strings[idKey - 1] = value
        chunk = []

        while self.list_strings[self.pointer]:
            chunk.append(self.list_strings[self.pointer])
            self.pointer += 1
        return chunk

      


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)