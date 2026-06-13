# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head :
            arr.append(head.val)
            head = head.next
        i = 0
        j = len(arr)-1 
        if arr == arr[::-1]:
            return True
        else :
            return False