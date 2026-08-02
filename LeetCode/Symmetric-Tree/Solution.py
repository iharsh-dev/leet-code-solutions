1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node_1,node_2):
10            if not node_1 and not node_2:
11                return True
12            if not node_1 or not node_2:
13                return False 
14            
15            if node_1.val != node_2.val:
16                return False 
17            
18            return dfs(node_1.right,node_2.left) and dfs(node_1.left,node_2.right)
19        return dfs(root.left,root.right)
20