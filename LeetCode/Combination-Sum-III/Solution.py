1class Solution:
2    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
3        ans = []
4        def recursion(ind, arr,num):
5            if num == k and sum(arr) == n:
6                ans.append(arr)
7                return 
8            if num > k:
9                return 
10            
11            for i in range(ind,10):
12                recursion(i + 1,arr + [i],num + 1)
13        
14        recursion(1,[],0)
15        return ans
16