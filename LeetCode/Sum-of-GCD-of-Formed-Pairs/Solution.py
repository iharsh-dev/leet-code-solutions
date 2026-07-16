1import math
2class Solution:
3    def gcdSum(self, nums: list[int]) -> int:
4        maxx = nums[0] 
5        pref = []
6        for i in nums:
7            maxx = max(maxx,i)
8            pref.append(math.gcd(i,maxx))
9        pref.sort()
10        i = 0 
11        j = len(pref)-1
12        some = 0
13        while i < j:
14            some+=(math.gcd(pref[i],pref[j]))
15            i+=1 
16            j-=1 
17        return some
18