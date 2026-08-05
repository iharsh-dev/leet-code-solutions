1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left < right:
6            mid = (left + right)//2
7            if nums[mid] == nums[right]:
8                right-=1
9            elif nums[mid] > nums[right]:
10                left = mid + 1
11            else:
12                right = mid 
13        return nums[left]