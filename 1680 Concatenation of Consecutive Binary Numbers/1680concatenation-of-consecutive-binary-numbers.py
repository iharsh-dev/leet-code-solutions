class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=""
        mod=10**9+7
        for i in range(1,n+1):
            b=bin(i)
            ans+=b[2:]
        return int(ans,2)%mod