class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        count = 0
        curr_sum = 0

        left, right, count = 0, len(people) - 1, 0
        curr_sum = people[left]

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                count += 1
            elif people[left] + people[right] > limit:
                right -= 1
                count += 1
            else:
                count += 1
                left += 1
            
        
        return count


            
                   