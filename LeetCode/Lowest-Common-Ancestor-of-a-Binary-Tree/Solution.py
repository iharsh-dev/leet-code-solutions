1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def dfs(node, p , q):
11            if not node:
12                return None
13            
14            if node == p:
15                return p
16            if node == q:
17                return q
18            
19            l = dfs(node.left, p,q) 
20            r = dfs(node.right, p,q)
21            if l and r:
22                return node
23            if l :
24                return l
25            if r:
26                return r
27        
28        return dfs(root,p,q)