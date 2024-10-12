# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd, even = ListNode(0), ListNode(0)
        result, tail = odd, even
        count = 1

        while head:
            node = ListNode(head.val)
            if count % 2 == 0:
                even.next = node
                even = even.next
            else:
                odd.next = node
                odd = odd.next
            
            head = head.next
            count += 1
        
        odd.next = tail.next
        odd = odd.next

        return result.next
        