# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0)
        curr, dummy = head, result 
        while curr:
            print(curr.val)
            if curr.val != val:
                dummy.next = ListNode(curr.val)
                dummy = dummy.next
            curr = curr.next
        
        return result.next