1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def bst(node,low,high):
10            if not node:
11                return True
12
13            if not (low < node.val < high):
14                return False
15
16            return bst(node.left,low,node.val) and bst(node.right, node.val,high)
17        
18        return bst(root,float('-inf'),float("inf"))