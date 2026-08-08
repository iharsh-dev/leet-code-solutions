1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left <= right:
6            mid = (left + right)//2
7            
8            if nums[mid] >= target:
9                right = mid - 1
10            else:
11                left = mid + 1
12        return left
13