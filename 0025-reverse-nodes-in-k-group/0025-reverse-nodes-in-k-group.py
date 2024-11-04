# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        nums, count, curr = [], 0, []

        while head:
            curr.append(head.val)
            head = head.next
            count += 1

            if count == k:
                nums.append(curr)
                curr, count = [], 0
        
        nums = [num[::-1] for num in nums]
        
        ans = ListNode(0)
        result = ans

        for num in nums:
            for n in num:
                node = ListNode(n)
                ans.next = node
                ans = ans.next
        if curr:
            for n in curr:
                node = ListNode(n)
                ans.next = node
                ans = ans.next

        return result.next
        