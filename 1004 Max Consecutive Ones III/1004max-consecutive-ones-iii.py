class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        zero = 0
        zoro = []
        arr = []
        b=0
        while j < n:
            if nums[j]==0:
                zoro.append(j)
                zero+=1
            if zero == k+1:
                arr.append(j-i)
                i = zoro[b]+1
                zero-=1
                b += 1
            j+=1
        arr.append(j-i)
        return max(arr)                
