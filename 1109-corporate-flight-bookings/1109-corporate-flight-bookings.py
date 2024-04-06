class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefix_sum = [0] * n

        for booking in bookings:
            first, last, seat = booking
            prefix_sum[first - 1] += seat
            if last < n:
                prefix_sum[last] -= seat

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i-1]
        
        return prefix_sum