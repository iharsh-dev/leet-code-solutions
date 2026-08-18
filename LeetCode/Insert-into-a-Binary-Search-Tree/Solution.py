1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        
10        
11        def dfs(node):
12            if not node:
13                return False
14            if node.val > val:
15                if not node.left:
16                    node.left = TreeNode(val,None,None)
17                    return True
18                if dfs(node.left):
19                    return True
20            else:
21                if not node.right:
22                    node.right = TreeNode(val,None,None)
23                    return True
24                if dfs(node.right):
25                    return True
26                   
27        dfs(root)
28        if not root:
29            root = TreeNode(val,None,None) 
30        return root