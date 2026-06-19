class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        maxx = 0
        for i in gain:
            curr += i
            maxx = max(maxx,curr)
        return maxx