class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        if not self.data:
            self.data.append(num)
        else:
            left, right = 0, len(self.data) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if self.data[mid] == num:
                    left = mid 
                    break
                if self.data[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        
            self.data.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.data)
        idx = n // 2
        if n % 2 == 0:
            return (self.data[idx] + self.data[idx - 1]) / 2
        
        return self.data[idx] 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()