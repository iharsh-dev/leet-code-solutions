1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        n = len(nums)
4        count = nums.count(val)
5        arr = []
6        for j in range(count):
7            nums.remove(val)
8            arr.append('_')
9        nums = nums + arr
10        return n - count