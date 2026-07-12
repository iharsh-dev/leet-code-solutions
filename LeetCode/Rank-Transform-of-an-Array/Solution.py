1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        brr = sorted(set(arr))
4        crr = {}
5        for i in range(len(brr)):
6            crr[brr[i]] = i+1
7        for i in range(len(arr)):
8            arr[i] = crr[arr[i]] 
9        return arr
10        