1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        if threshold < len(nums):
4            return -1
5
6        left = 1
7        right = max(nums)
8
9        while left < right:
10
11            mid = (left+right)//2 
12            ans = 0
13
14            for i in nums:
15                ans += (i + mid - 1)//mid
16                if ans > threshold:
17                    break
18            if ans > threshold:
19                left = mid + 1
20            else:
21                right = mid 
22        
23        return right
24