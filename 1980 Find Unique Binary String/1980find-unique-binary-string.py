class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans=[]
        n=len(nums)
        for i in range(n):
            if nums[i][i]=='1':
                ans.append('0')
            else:
                ans.append('1')
        return "".join(ans)