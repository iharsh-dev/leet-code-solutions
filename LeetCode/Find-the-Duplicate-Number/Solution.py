1from collections import defaultdict
2class Solution:
3    def findDuplicate(self, nums: List[int]) -> int:
4        freq = defaultdict(int)
5
6        for i in nums:
7            if not freq[i]:
8                freq[i] = 1 
9            else:
10                return i