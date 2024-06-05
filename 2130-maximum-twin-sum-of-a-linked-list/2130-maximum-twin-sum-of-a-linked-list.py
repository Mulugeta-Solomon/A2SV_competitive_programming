# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rev_head, curr = None, slow

        while curr:
            next_node = curr.next
            curr.next = rev_head
            rev_head = curr
            curr = next_node
        
        max_twin_sum =  float('-inf')

        while rev_head:
            max_twin_sum = max(max_twin_sum, head.val + rev_head.val)
            rev_head = rev_head.next
            head = head.next
        
        return max_twin_sum





        