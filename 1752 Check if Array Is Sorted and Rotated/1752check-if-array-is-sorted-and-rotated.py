class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        og = nums[:]
        og.sort()
        for i in range(n):
            if nums == og[i:]+og[:i]:
                return True
        return False