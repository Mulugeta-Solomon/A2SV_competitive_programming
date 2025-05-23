class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [] 
        self.size = k


    def enQueue(self, value: int) -> bool:
        if self.size > 0:
            self.queue.append(value)
            self.size -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            self.size += 1
            return True
        return False
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.queue
        
    def isFull(self) -> bool:
        return self.size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()