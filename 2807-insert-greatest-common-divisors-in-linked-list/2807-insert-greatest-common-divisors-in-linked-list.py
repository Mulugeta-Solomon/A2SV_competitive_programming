# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        while curr and curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val))

            temp = curr.next 
            curr.next = new_node
            new_node.next = temp
            curr = new_node.next
        
        return head