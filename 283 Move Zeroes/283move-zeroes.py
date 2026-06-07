class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        j = 1
        while j < n:
            if nums[i] == 0 :
                if nums[j] != 0 :
                    nums[i],nums[j] = nums[j],nums[i]
                else:
                    j+=1
            else:
                i+=1
                j+=1

        