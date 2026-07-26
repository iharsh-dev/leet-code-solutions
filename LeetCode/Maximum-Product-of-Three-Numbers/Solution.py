1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums.sort(reverse = True)
4        return max(nums[0]*nums[1]*nums[2], nums[-1]*nums[-2]*nums[0])