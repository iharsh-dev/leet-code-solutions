1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        n = len(lists)
9        ans = []
10        dummy = None
11        tail = dummy
12        while True:
13            check = False
14            minn = 10**4+1
15            ind = 0
16            for i in range(n):
17                if lists[i] != None:
18                    check = True 
19                    c = lists[i].val 
20                    if c < minn:
21                        minn = c
22                        ind = i
23            if check:
24                if len(ans) == 0:
25                    ans.append(lists[ind])
26                    dummy = ans[-1]
27                    tail = dummy
28                else:
29                    tail.next = lists[ind]
30                    tail = tail.next
31                lists[ind] = lists[ind].next
32            else:
33                if tail:
34                    tail.next = None
35                return dummy
36
37
38