# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1, num_2 = '', ''

        head_1, head_2 = l1, l2

        while head_1:
            num_1 += str(head_1.val)
            head_1 = head_1.next
        
        
        while head_2:
            num_2 += str(head_2.val)
            head_2 = head_2.next
        
        num_1 = num_1[::-1]
        num_2 = num_2[::-1]
        total = str(int(num_1) + int(num_2))[::-1]
        # print(total)
  
        head = ListNode(int(total[0]))
        temp = head
        for i in range(1,len(total)):
            head.next = ListNode(int(total[i]))
            head = head.next
        
        return temp


        
        