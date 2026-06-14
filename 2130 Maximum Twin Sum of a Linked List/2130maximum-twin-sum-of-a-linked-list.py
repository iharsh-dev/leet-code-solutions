# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head 
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nex = slow.next 
            slow.next = prev
            prev = slow 
            slow = nex 
        ans = 0
        while prev :
            ans = max(ans,prev.val+head.val)
            head = head.next
            prev = prev.next 
        return ans
