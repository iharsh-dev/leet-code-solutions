class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=[0]*3
        for i in nums:
            count[i]+=1
        j=0
        i=0
        while i<len(nums):
            for m in range(count[j]):
                nums[i]=j
                i+=1
            j+=1

        