"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def recursion(curr):
            
            while curr:
                if not curr.next and not curr.child:
                    return curr

                temp = curr.next if curr.next else None
                if curr.child:
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None

                    curr = curr.next
                    last = recursion(curr)
                    if last:
                        last.next = temp
                    if temp:
                        temp.prev = last
                    curr = temp
                    if not curr:
                        return last
                    continue 

                curr.next = temp
                curr = curr.next
        
        curr = head 
        recursion(curr)

        return head

        