class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        left, right = 0, len(a) - 1
        
        # case_1
        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        else:
            left_b, right_b = left, right
            flag1, flag2 = False, False
            
            while left < right and a[left] == a[right]:
                left += 1
                right -= 1
            
            if left >= right:
                flag1 = True
            
            while left_b < right_b and b[left_b] == b[right_b]:
                left_b += 1
                right_b -= 1

            if left_b >= right_b:
                flag2 = True
        
            flag_case_1 = flag1 or flag2

        
        # case_2
        left, right = 0, len(a) - 1

        while left < right and b[left] == a[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        else:
            left_b, right_b = left, right
            flag1, flag2 = False, False
            
            while left < right and a[left] == a[right]:
                left += 1
                right -= 1
            
            if left >= right:
                flag1 = True
            
            while left_b < right_b and b[left_b] == b[right_b]:
                left_b += 1
                right_b -= 1

            if left_b >= right_b:
                flag2 = True
        
            flag_case_2 = flag1 or flag2

        return flag_case_1 or flag_case_2
