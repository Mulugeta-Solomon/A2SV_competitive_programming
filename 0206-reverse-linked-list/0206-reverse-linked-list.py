# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_node = head 
        prev_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node






        # alst = []
        # curr_node = self.head
        # print(curr_node)
        # while curr_node:
        #     alst.append(curr_node.val)
        #     curr_node = curr_node.next

        # print(alst)
        # alst = alst[::-1]
        # curr_node = ListNode(alst[0])
        
        # for i in range(1, len(alst)):
        #     node = ListNode(alst[i])
        #     curr_node.next = node
        #     node.prev = curr_node








     
            






        