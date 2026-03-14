class Solution:
    def perma(self,ans,s,n):
        if len(s)==n:
            ans.append(s)
        else:
            if s[-1]=='a':
                self.perma(ans,s+'b',n)
                self.perma(ans,s+'c',n)
            elif s[-1]=='b':
                self.perma(ans,s+'a',n)
                self.perma(ans,s+'c',n)
            else:
                self.perma(ans,s+'a',n)
                self.perma(ans,s+'b',n)
    def getHappyString(self, n: int, k: int) -> str:
        ans=[]
        self.perma(ans,'a',n)
        self.perma(ans,'b',n)
        self.perma(ans,'c',n)
        ans.sort()
        if k>len(ans):
            return ""
        else:
            return ans[k-1]