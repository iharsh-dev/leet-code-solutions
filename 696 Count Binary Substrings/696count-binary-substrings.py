class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr=list(map(int,s))
        prev_group=0
        ans=0
        i=0
        while i<len(arr)-1:
            current_group=1
            while i<len(arr)-1 and arr[i]==arr[i+1]:
                current_group+=1
                i+=1
            ans+=min(current_group,prev_group)
            prev_group=current_group
            i+=1
        if len(arr)>1 and arr[-1]!=arr[-2]:
            ans+=1
        return ans
                