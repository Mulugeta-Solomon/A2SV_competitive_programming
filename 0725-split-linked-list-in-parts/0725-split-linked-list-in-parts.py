# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr, length = head, 0

        while curr:
            curr = curr.next
            length += 1

        result, part_size, remainder  = [], length // k, length % k 

        curr = head
        for i in range(k):
            part, n = curr, part_size - 1 + (i < remainder)
            
            while n > 0:
                if curr:
                    curr = curr.next
                n -= 1

            if curr:
                next = curr.next
                curr.next = None
                curr = next

            result.append(part)
        
        return result


