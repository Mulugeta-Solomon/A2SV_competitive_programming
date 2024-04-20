"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        look_up = {None:None}
        dummy = Node(0)
        deep_copy = dummy
        curr = head 
        while curr:
            deep_copy.next = Node(curr.val)
            if curr not in look_up:
                look_up[curr] = deep_copy.next
            curr = curr.next
            deep_copy = deep_copy.next

        curr, deep_copy = head, dummy.next
        while curr:
            if curr in look_up:
                deep_copy.random = look_up[curr.random]
            curr = curr.next
            deep_copy = deep_copy.next
            
        return dummy.next



