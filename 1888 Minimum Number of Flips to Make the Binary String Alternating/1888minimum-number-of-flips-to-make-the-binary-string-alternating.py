class Solution:
    def minFlips(self, s: str) -> int:
        odd_1=0
        odd_0=0
        even_1=0
        even_0=0
        n=len(s)
        for i in range(len(s)):
            if i % 2 !=0:
                if s[i]=='1':
                    odd_1+=1
                else:
                    odd_0+=1
            else:
                if s[i]=='1':
                    even_1+=1
                else:
                    even_0+=1
        j=0
        min_=[]
        if n%2!=0:
            while j<n:
                min_.append(min(odd_1+even_0,odd_0+even_1))
                if s[j]=='1':
                    even_1-=1
                    odd_1,even_1=even_1,odd_1
                    odd_0,even_0=even_0,odd_0
                    even_1+=1
                else:
                    even_0-=1
                    odd_1,even_1=even_1,odd_1
                    odd_0,even_0=even_0,odd_0
                    even_0+=1
                j+=1
        else:
            while j<n:
                min_.append(min(odd_1+even_0,odd_0+even_1))
                if s[j]=='1':
                    even_1-=1
                    odd_1,even_1=even_1,odd_1
                    odd_0,even_0=even_0,odd_0
                    odd_1+=1
                else:
                    even_0-=1
                    odd_1,even_1=even_1,odd_1
                    odd_0,even_0=even_0,odd_0
                    odd_0+=1
                j+=1
        return min(min_)