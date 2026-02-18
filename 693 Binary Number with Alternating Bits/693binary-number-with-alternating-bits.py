class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num=bin(n)[2:]
        check=0
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                check=1
                break
        if check==1:
            a=False
        else:
            a=True
        return a