# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, n = head, 0

        while curr:
            curr = curr.next
            n += 1
        
        if n <= 1:
            return None

        target, result = math.floor(n / 2), head
        head = result
        
        while target > 1:
            result = result.next
            target -= 1
        
        result.next = result.next.next

        return  head


