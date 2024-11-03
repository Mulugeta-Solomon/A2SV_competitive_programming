# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        pairs, result = [], ListNode(0)
        pair, curr = [], result
        while head:
            pair.append(head.val)
            head = head.next
            if len(pair) == 2:
                pairs.append(pair)
                pair = []
        
        if pair:
            pairs.append(pair)
        
        pairs = [pair[::-1] for pair in pairs]
        
        for pair in pairs:
            for num in pair:
                node = ListNode(num)
                curr.next = node
                curr = curr.next

        return result.next 

