class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            a = bin(n)
            b = a[2:]
            c = [ int(i) for i in b]
            if sum(c)==1:
                return True
            else:
                return False
        else:
            return False
        