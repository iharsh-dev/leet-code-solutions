1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        summ = -1001
10        def dfs(node):
11            if not node:
12                return 0 
13            l = dfs(node.left)
14            r  = dfs(node.right)
15            nonlocal summ
16            summ = max(summ,max(0,l) + max(0,r) + node.val)
17            return node.val + max(0,l,r)
18        dfs(root)
19        return summ