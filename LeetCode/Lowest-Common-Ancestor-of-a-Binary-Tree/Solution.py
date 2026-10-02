1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root:
11            return None
12        
13        if root == p:
14            return p
15        
16        if root == q:
17            return q
18        
19        left = self.lowestCommonAncestor(root.left,p,q)
20        right = self.lowestCommonAncestor(root.right,p,q)
21
22        if left and right:
23            return root
24
25        return left or right
26        
27