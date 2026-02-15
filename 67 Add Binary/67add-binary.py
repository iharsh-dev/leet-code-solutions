class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al=list(int(m) for m in a)
        bl=list(int(k) for k in b)
        al.reverse()
        bl.reverse()
        carry=0
        ans=""
        n=max(len(al),len(bl))
        for i in range(n):
            if i<len(al) and i<len(bl):
                c=al[i]+bl[i]+carry
            elif i>=len(al) and i<len(bl):
                c=bl[i]+carry
            elif i>=len(bl) and i<len(al):
                c=al[i]+carry
            if c==3:
                ans+='1'
                carry=1
            elif c==2:
                ans+='0'
                carry=1
            elif c==1:
                ans+='1'
                carry=0
            else:
                ans+='0'
                carry=0
        if carry==1:
            ans+='1'
        app=ans[::-1]
        return app
            
