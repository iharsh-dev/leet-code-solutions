# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        if head :
            fast = head.next 
        else:
            fast = None
        check = False
        while fast :
            if fast == slow :
                check = True 
                break
            if slow : 
                slow = slow.next 
            else:
                break
            if fast.next : 
                fast = fast.next.next 
            else:
                break
        return check
            