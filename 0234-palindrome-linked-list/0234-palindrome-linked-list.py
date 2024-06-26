# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        curr = head 
        while curr:
            nums.append(curr.val)
            curr = curr.next

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] != nums[right]:
                return False 
            left += 1
            right -= 1
        
        return True