class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.idx = -1
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.idx < len(self.stack) - 1:
            self.idx += 1
            self.stack[self.idx] = x

    def pop(self) -> int:
        if self.idx != -1:
            result = self.stack[self.idx]
            self.idx -= 1

            return result 
        return -1

    def increment(self, k: int, val: int) -> None:
        if k < self.maxSize:
            i = 0
            while i < k:
                self.stack[i] += val
                i += 1
            
        else:
            i = 0
            while i < self.maxSize:
                self.stack[i] += val
                i += 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)