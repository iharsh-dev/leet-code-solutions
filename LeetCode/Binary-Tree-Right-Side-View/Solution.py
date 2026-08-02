1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        if not root:
11            return []
12        que = deque([root])
13        side_view = []
14        while que:
15            level = []
16            n = len(que)
17            for _ in range(n):
18                node = que.popleft()
19                level.append(node.val)
20                if node.left:
21                    que.append(node.left)
22                if node.right:
23                    que.append(node.right)
24            side_view.append(level[-1])
25        return side_view