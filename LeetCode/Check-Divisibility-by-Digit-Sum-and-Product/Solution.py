1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        arr = [int(i) for i in str(n)]
4        prod = 1
5        summ = 0
6        for i in arr:
7            prod *= i
8            summ += i 
9        
10        return True if not n % (prod + summ) else False
11