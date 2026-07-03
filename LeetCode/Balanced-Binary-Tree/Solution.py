1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(root):
10            if root == None:
11                return 0 
12            return max(dfs(root.left),dfs(root.right))+1
13        if root == None:
14            return True
15        if abs(dfs(root.left) - dfs(root.right))<=1:
16            return self.isBalanced(root.left)&self.isBalanced(root.right)
17        else:
18            return False