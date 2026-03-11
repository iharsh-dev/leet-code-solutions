class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=bin(n)
        c=a[2:]
        b=""
        for i in c:
            if i=='1':
                b+='0'
            else:
                b+='1'
        return int(b,2)
