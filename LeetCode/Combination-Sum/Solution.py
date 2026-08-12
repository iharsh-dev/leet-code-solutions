1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        ans = []
4        def function(ind, some,arr):
5            if some == target:
6                ans.append(arr)
7                return
8            if some > target:
9                return
10            for i in range(ind,len(candidates)):
11                function(i,some + candidates[i], arr + [candidates[i]])
12        
13        function(0,0,[])
14        return ans