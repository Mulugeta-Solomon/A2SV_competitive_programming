# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def converToArray(self, head):
        curr, nums = head, []
        while curr:
            nums.append(curr)
            curr = curr.next 
        
        return nums
    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = self.converToArray(head)
        
        nums[k - 1], nums[len(nums) - k] = nums[len(nums) - k], nums[k - 1]
        
        for i in range(len(nums) - 1):
            nums[i].next = nums[i+1] 
        
        nums[-1].next = None

        return nums[0]



        
        return head
        

        