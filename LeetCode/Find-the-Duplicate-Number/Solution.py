1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        fast = nums[0]
4        slow = nums[0]
5        while True:
6            slow = nums[slow]
7            fast = nums[nums[fast]]
8            if slow == fast:
9                break
10
11        slow = nums[0]
12        while slow!=fast:
13            fast = nums[fast]
14            slow = nums[slow]
15        return slow