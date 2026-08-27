1from collections import defaultdict
2class Solution:
3    def subarraysDivByK(self, nums: List[int], k: int) -> int:
4        hash_map = defaultdict(int)
5        hash_map[0] = 1
6        ans = 0
7        curr = 0
8
9        for num in nums:
10            curr = curr + num
11
12            rem = curr % k
13            ans+=hash_map[rem]
14            hash_map[rem]+=1
15        
16        return ans