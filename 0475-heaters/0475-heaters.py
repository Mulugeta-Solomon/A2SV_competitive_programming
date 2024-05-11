class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        left, right = 0, 10 ** 9
        radiusStandard = -1
        houses.sort()
        heaters.sort()

        while left <= right:
            mid = left + (right - left) // 2

            if self.isValid(mid, houses, heaters):
                radiusStandard = mid 
                right = mid - 1
            else:
                left = mid + 1 
        
        return radiusStandard
    
    def isValid(self, mid: int, houses: List[int], heaters: List[int]) -> bool:
        heater_ptr, house_ptr = 0, 0

        while heater_ptr < len(heaters) and house_ptr < len(houses):

            if abs(heaters[heater_ptr] - houses[house_ptr]) <= mid:
                house_ptr += 1
            else:
                heater_ptr += 1
        
        return heater_ptr < len(heaters)

