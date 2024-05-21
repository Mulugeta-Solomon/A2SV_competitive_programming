class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons 
        self.times = times
        self.leads = [0] * len(self.times)

        count, lead = {}, -1
        for i in range(len(self.persons)):
            count[self.persons[i]] = count.get(self.persons[i], 0) + 1

            if count[self.persons[i]] >= count.get(lead, 0):
                lead = self.persons[i]
            
            self.leads[i] = lead

    def q(self, t: int) -> int:

        indx = bisect_right(self.times, t) - 1

        return self.leads[indx]

    def binarySearch(self, target) -> int:
        left, right =  0, len(self.times) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print(mid, target)

            if self.times[mid] > target and self.times[mid - 1] < target:
                return mid - 1

            if mid >= len(self.times) - 1 or self.times[mid] == target:
                return mid
            elif self.times[mid] > target:
                right = mid - 1
            else:
                left = mid + 1



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)