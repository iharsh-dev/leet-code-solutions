1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def treetraversal(self, node , arr):
9        if node == None:
10            return 
11        arr.append(node.val)
12        self.treetraversal(node.left,arr)
13        self.treetraversal(node.right,arr)
14        return
15    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
16        arr = []
17        self.treetraversal(root,arr)
18        return arr