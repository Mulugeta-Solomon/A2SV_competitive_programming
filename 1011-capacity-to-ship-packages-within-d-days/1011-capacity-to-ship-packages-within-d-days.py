class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        least_weight_cap = -1

        while left <= right:
            mid = left + (right - left) // 2

            if self.canCarryWithinDays(weights, mid, days):
                least_weight_cap = mid 
                right = mid - 1
            else:
                left = mid + 1
            
        return least_weight_cap
    
    def canCarryWithinDays(self, weights: List[int], capacity: int, days: int) -> bool:
        curr_days, curr_capacity = 1, 0

        for weight in weights:
            if curr_capacity + weight > capacity:
                curr_days += 1
                curr_capacity = 0

            curr_capacity += weight
        
        return curr_days <= days

        