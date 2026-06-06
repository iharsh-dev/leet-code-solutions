class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        some = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = some - left - nums[i]
            answer.append(abs(right - left))
            left += nums[i] 
        return answer
