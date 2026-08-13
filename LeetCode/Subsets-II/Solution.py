1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        n = len(nums)
4        ans = []
5        nums.sort()
6        def subset(ind,arr):
7            ans.append(arr)
8            for i in range(ind,n):
9                if i > ind and nums[i] == nums[i-1]:
10                    continue
11                
12                subset(i + 1, arr + [nums[i]])
13            
14        subset(0,[])
15        return ans
16                
17