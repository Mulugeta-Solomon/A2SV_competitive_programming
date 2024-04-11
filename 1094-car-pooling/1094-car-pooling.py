class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix_sum = [0] * (1001)

        for i in range(len(trips)):
            num_passengers, from_, to = trips[i]
            prefix_sum[from_] += num_passengers
            prefix_sum[to] -= num_passengers
        print(prefix_sum[:10])
        for right in range(len(prefix_sum)):
            prefix_sum[right+1] += prefix_sum[right]

            if right > 0 and prefix_sum[right] == 0:
                break 
        print(prefix_sum[:10])
        for right in range(len(prefix_sum)):
            if prefix_sum[right] > capacity:
                return False
            
            if right > 0 and prefix_sum[right] == 0:
                break 
        
        return True 
