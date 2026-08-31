1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        curr = head.next
9        prev = head
10        minn = float('inf')
11        maxx = 0
12        check = False
13        consec = 0
14        count = 0
15
16        while curr and curr.next:
17            if check:
18                count += 1
19                consec += 1
20
21            if (curr.val < curr.next.val and curr.val < prev.val) or (curr.val > curr.next.val and curr.val > prev.val):
22                if check:
23                    minn = min(minn,consec)
24                    maxx = max(maxx,count)
25                check = True
26                consec = 0
27            
28            prev = curr
29            curr = curr.next
30        
31        return [minn,maxx] if maxx != 0 else [-1,-1]
32            
33
34
35