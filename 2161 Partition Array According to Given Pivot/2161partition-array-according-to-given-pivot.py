class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        more = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot :
                equal.append(i)
            else : 
                more.append(i)
        ans = less + equal + more 
        return ans