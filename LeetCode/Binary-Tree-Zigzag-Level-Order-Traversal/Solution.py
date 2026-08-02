1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        if not root:
11            return []
12
13
14        queue = [root]
15        ans = []
16        count = 0
17        while queue:
18            level = []
19            order = []
20            n = len(queue)
21            for i in range(n):
22                if queue[i]:
23                    level.append(queue[i].val)
24                    order.append(queue[i].left)
25                    order.append(queue[i].right)
26            queue = order[:]
27            level = level[::-1] if count%2 != 0 else level
28            if len(level) > 0:
29                ans.append(level)
30            count+=1
31        return ans
32                    