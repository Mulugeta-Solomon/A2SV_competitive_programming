# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        merged_list = dummy 

        curr_1, curr_2 = list1, list2

        while curr_1 or curr_2:
            if curr_1 and curr_2:
                if curr_1.val >= curr_2.val:
                    dummy.next = curr_2
                    curr_2 = curr_2.next
                else:
                    dummy.next = curr_1
                    curr_1 = curr_1.next
            else:
                if not curr_1:
                    dummy.next = curr_2
                    curr_2 = curr_2.next
                else:
                    dummy.next = curr_1
                    curr_1 = curr_1.next
            dummy = dummy.next
        dummy.next = None

        return merged_list.next


