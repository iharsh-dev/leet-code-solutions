class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a_=bin(nums[0])
        a=a_[2:]
        b_=bin(nums[1])
        b=b_[2:]
        c_=bin(nums[2])
        c=c_[2:]
        num=[0]*6
        num[0]=a+b+c
        num[1]=a+c+b
        num[2]=b+a+c
        num[3]=b+c+a
        num[4]=c+a+b
        num[5]=c+b+a
        ans = [ int(i,2) for i in num]
        return max(ans)
