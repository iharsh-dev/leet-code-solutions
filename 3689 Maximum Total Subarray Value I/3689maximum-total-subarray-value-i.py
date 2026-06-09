class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = k*(max(nums)-min(nums))
        return ans