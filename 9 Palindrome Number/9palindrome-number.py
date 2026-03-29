class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            a=[ i for i in str(x)]
            i=0
            j=len(a)-1
            check=True
            while i<j:
                if a[i]!=a[j]:
                    check=False
                    break
                i+=1
                j-=1
            return check