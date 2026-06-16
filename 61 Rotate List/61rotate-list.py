# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next 
        k = k%length if length > 0 else 0
        if length > 1 and k > 0:
            
            curr = head
            prev = None
            for i in range(length - k):
                prev = curr
                curr = curr.next 
            
            tail.next = head
            head = curr 
            prev.next = None 

        return head