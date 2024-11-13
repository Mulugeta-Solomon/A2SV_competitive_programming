# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, wind_sum = head, head.next, 0

        while curr:
            if curr.val == 0:
                prev.next.val = wind_sum
                prev, wind_sum = prev.next, 0
                
            wind_sum += curr.val 
            curr = curr.next
        
        prev.next = None 
        prev = prev.next
        
        return head.next