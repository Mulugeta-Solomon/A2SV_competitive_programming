# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr_node, prev_node = head, None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1, l2 = self.reverse(l1), self.reverse(l2)

        dummy = ListNode(0)
        result = dummy

        curr_sum, carry = 0, 0

        while l1 or l2:
            if l1 and l2:
                curr_sum = l1.val + l2.val + carry 
                dummy.next = ListNode(curr_sum % 10)
                carry = curr_sum // 10
                l1, l2 = l1.next, l2.next
            else:
                if not l1:
                    curr_sum = l2.val + carry 
                    dummy.next = ListNode(curr_sum % 10)
                    carry = curr_sum // 10
                    l2 = l2.next
                else:
                    curr_sum = l1.val + carry 
                    dummy.next = ListNode(curr_sum % 10)
                    carry = curr_sum // 10
                    l1 = l1.next
            dummy = dummy.next
        
        if carry > 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        
        result = self.reverse(result.next)

        return result



