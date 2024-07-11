# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for linkedlist in lists:
            node = linkedlist
            curr = []
            
            while node:
                heappush(curr, node.val)
                node = node.next
            
            heap.extend(curr)
        
        heap.sort()

        if heap:
            head = ListNode(heap[0])
            curr = head 
            for num in heap[1:]:
                curr.next = ListNode(num)
                curr = curr.next
            
            return head

        return None
            