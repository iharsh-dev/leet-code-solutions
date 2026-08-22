1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        prod = 1
4        summ = 0
5        for i in str(n):
6            prod *= int(i)
7            summ += int(i) 
8        
9        return True if not n % (prod + summ) else False
10