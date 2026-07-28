1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        n = len(cardPoints)
4        window = n-k
5        some = sum(cardPoints[:window])
6        ans = some
7        for i in range(window,n):
8            some = some + cardPoints[i] - cardPoints[i - window]
9            ans = min(ans,some)
10        return sum(cardPoints) - ans
11