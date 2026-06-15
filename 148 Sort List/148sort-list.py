# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head 
        while curr:
            arr.append(curr.val)
            curr = curr.next 
        arr.sort()
        curr = head 
        a = 0
        while curr :
            curr.val = arr[a]
            curr = curr.next 
            a+=1 
        return head