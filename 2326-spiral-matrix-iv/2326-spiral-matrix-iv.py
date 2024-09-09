# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        top, bottom, right, left = 0, m - 1, n - 1, 0
        curr = head

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result[top][col] = curr.val 
                curr = curr.next
                if not curr:
                    return result
            top += 1

            for row in range(top, bottom + 1):
                result[row][right] = curr.val 
                curr = curr.next
                if not curr:
                    return result 
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result[bottom][col] = curr.val
                    curr = curr.next 
                    if not curr:
                        return result 
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result[row][left] = curr.val 
                    curr = curr.next 
                    if not curr:
                        return result 
                left += 1
        
        return result 




        