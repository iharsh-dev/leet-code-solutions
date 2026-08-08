1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        i = m - 1
4        j = n - 1
5        while i >= 0 and j >= 0:
6            if nums1[i] > nums2[j]:
7                nums1[i + j + 1] = nums1[i]
8                i-=1
9            else:
10                nums1[i + j + 1] = nums2[j]
11                j-=1
12        for k in range(j , -1, -1):
13            nums1[i + k + 1] = nums2[k]
14        