1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        new = nums1+nums2
4        new.sort()
5        n = len(new)
6        if n % 2 == 0:
7            return (new[(n-1)//2]+new[n//2])/2 
8        
9        return new[n//2]