1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import defaultdict
8class Solution:
9    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
10        tree = defaultdict(list)
11        def dfs(node , col , row):
12            if not node:
13                return 
14            tree[col].append((row,node.val))
15            dfs(node.left, col - 1, row + 1)
16            dfs(node.right,col + 1, row + 1)
17        dfs(root,0, 0)
18        s_tree = dict(sorted(tree.items()))
19        for key in s_tree:
20            s_tree[key].sort()
21
22        ans = []
23        for key in s_tree:
24            arr = []
25            for row, value in s_tree[key]:
26                arr.append(value)
27            ans.append(arr)
28        
29        return ans