1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
4        f = Counter(nums)
5        freq = dict(sorted(f.items(),key = lambda x:x[1],reverse = True))
6        ans = []
7        for key in freq:
8            ans.append(key)
9            k-=1
10            if k == 0:
11                break
12        
13        return ans
14
15
16        