1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        f = Counter(nums)
5        freq = dict(sorted(f.items(), key = lambda x:x[1],reverse = True))
6        ans = []
7        for key in freq:
8            if not k:
9                break
10            ans.append(key)
11            k-=1 
12        return ans