1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from functools import cache
8class Solution:
9    def rob(self, root: Optional[TreeNode]) -> int:
10        @cache
11        def dfs(node):
12            if not node:
13                return [0,0]
14            dp = [dfs(node.left),dfs(node.right)]
15            return [dp[0][1]+ dp[1][1] + node.val,max(dp[0])+max(dp[1])]
16        return max(dfs(root))