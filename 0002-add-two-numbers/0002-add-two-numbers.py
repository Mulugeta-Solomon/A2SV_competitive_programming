# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        result = dummy 

        carry, curr_sum = 0, 0

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
        
        dummy.next = None 

        return result.next