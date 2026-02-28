class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        arr=[ i for i in s]
        i=0
        while i<len(arr):
            j=i+1
            while j<len(arr) and j<=i+k:
                if arr[i]==arr[j]:
                    del arr[j]
                    i=-1
                    break
                else:
                    j+=1
            i+=1
        ans="".join(arr)
        return ans
               