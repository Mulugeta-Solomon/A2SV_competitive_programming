class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        times, waitingTime = [0] * len(customers), 0

        for i, (arrival, time) in enumerate(customers):
            if i == 0 or times[i - 1] < arrival:
                times[i] = arrival + time
                continue
        
            times[i] = times[i - 1] + time 

        for i in range(len(customers)):
            waitingTime += (times[i] - customers[i][0])


        return waitingTime / len(customers)