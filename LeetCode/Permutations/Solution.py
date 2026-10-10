1from itertools import permutations
2class Solution:
3    def permute(self, nums: list[int]) -> list[list[int]]:
4        return list(permutations(nums))