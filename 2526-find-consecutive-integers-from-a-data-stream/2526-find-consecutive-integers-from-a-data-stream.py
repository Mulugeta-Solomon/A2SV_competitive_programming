class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value 
        self.k = k
        self.queue = []

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        
        if len(self.queue) < self.k:
            return False 
        
        right = len(self.queue) - 1
        left = right - self.k + 1

        while left <= right:
            if self.queue[left] != self.value:
                return False
            left += 1

        return True 

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)