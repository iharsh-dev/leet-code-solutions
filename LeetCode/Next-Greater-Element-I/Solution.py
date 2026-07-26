1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        dic = {}
4        n = len(nums2)
5        for i in range(n):
6            dic[nums2[i]] = i 
7        ans = [-1]*len(nums1)
8        for i in range(len(nums1)):
9            for j in range(dic[nums1[i]] + 1, n):
10                if nums2[j] > nums1[i]:
11                    ans[i] = nums2[j]
12                    break 
13        return ans