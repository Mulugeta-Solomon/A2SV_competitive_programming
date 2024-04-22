# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result = ListNode(0, head) # create dummy node 

        left_prev, curr = result, head 
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next
        
        prev, curr = None, curr 
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node 
        
        left_prev.next.next = curr 
        left_prev.next = prev 

        return result.next




