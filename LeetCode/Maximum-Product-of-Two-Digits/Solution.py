1class Solution:
2    def maxProduct(self, n: int) -> int:
3        arr = [int(i) for i in str(n)]
4        arr.sort(reverse = True)
5        return arr[0]*arr[1]