class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = n-2
        j = n-1
        count=0
        while i >= 0:
            maxx=-1
            ind=0
            for k in range(i,-1,-1):
                c = nums[k]+k
                if c >= j and j-k > maxx:
                    maxx=j-k
                    ind=k
            j=ind
            i=j-1
            count+=1
        return count
            
            
            