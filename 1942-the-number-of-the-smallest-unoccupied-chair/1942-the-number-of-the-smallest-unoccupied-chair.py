class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times_idx = [times[i] + [i] for i in range(len(times))]
        

        times_idx.sort(key=lambda x:x[0])
        leaveHeap, availChair = [], []
        heappush(availChair, 0)

        for i, time in enumerate(times_idx):
            arrv, leav, friend = time
            while leaveHeap and arrv >= leaveHeap[0][0]:
                heappush(availChair, leaveHeap[0][1])
                heappop(leaveHeap)
            
            if friend == targetFriend:
                return heappop(availChair)
            
            heappush(leaveHeap, [leav, heappop(availChair)])
            if not availChair:
                heappush(availChair, len(leaveHeap))


