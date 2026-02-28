class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        arr=[0]*101
        nums.sort()
        for i in nums:
            arr[i]+=1
        ans=[-1,-1]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if arr[nums[i]]!=arr[nums[j]]:
                    ans[0]=nums[i]
                    ans[1]=nums[j]
                    break
            if ans[0]==nums[i]:
                break
        return ans