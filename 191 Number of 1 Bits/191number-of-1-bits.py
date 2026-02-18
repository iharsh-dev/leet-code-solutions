class Solution:
    def hammingWeight(self, n: int) -> int:
        num=bin(n)[2:]
        lisp=list(map(int,num))
        b=sum(lisp)
        return b