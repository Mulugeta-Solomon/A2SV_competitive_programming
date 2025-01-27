# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        result, lookup, curr = 0, set(nums), head
        conn_comp = set()

        while curr:
            if curr.val in lookup:
                conn_comp.add(curr.val)
            if (curr.val not in lookup and conn_comp) or (curr.val in lookup and not curr.next):
                result += 1
                conn_comp = set()
            curr = curr.next
        
        return result
        