class Solution:
    def maximumLength(self, s: str) -> int:
        
        def is_possible(n):
            lookUp, left = defaultdict(int), 0

            while left + n <= len(s) :
                if len(set(s[left:left + n])) == 1:
                    lookUp[s[left:left + n]] += 1
                left += 1

            for val in lookUp.values():
                if val >= 3:
                    return True
            
            return False 

        left, right, result = 1, len(s) - 1, -1

        while left <= right:
            mid = left + (right - left) // 2

            if is_possible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result  
