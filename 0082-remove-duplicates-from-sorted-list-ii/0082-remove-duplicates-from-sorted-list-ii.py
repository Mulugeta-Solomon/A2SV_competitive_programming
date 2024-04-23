# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-101, head)
        result = dummy 
        curr, prev = head, dummy 
        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = prev.next

                if curr.next:
                    if prev.val != curr.next.val:
                        dummy.next = prev 
                        dummy = dummy.next 
                else:
                        dummy.next = prev 
                        dummy = dummy.next 
                
            curr = curr.next
        
        dummy.next = None 
        return result.next



        